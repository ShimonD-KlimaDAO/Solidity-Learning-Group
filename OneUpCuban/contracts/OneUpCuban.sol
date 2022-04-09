// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

import "../interfaces/IKlimaRetirementAggregator.sol";
import "../interfaces/IERC20.sol";

import "@openzeppelin/contracts/access/Ownable.sol";

contract OneUpCuban is Ownable {

    uint public minDeposit;
    uint public targetAmount;
    uint public balance;
    uint public CubanCount;
    
    address public immutable KlimaRetirementAggregator;
    address public immutable BCT;

    mapping(uint => address) public winners;

    constructor() {

        KlimaRetirementAggregator = 0xEde3bd57a04960E6469B70B4863cE1c9d9363Cb8;
        BCT = 0x2F800Db0fdb5223b3C3f354886d907A671414A7F;
        targetAmount =  102020202020202020202 ; /* amount corresponding to 101 BCT after 1% Klima fee */
        minDeposit =    0; 
        
    }


    function deposit(uint amount) public {

        require(amount >= minDeposit, "Cannot deposit less than mindeposit");
        require(IERC20(BCT).allowance(msg.sender, address(this)) >= amount, "Contract must have sufficient spending allowance of BCT amount");

        IERC20(BCT).transferFrom(msg.sender, address(this), amount);
        
        updateBCTBalance();

        if (balance >= targetAmount) {

            _offsetBalance(targetAmount, "#1UpCuban", "Cuban was one-upped!");

            /* set winner */
            winners[CubanCount] = msg.sender;

            /* send remaining change to winner */
            _sendExtra();

            /* Increment Cuban count */
            CubanCount++;

        }

    }

    function updateBCTBalance() public {

        /* Update current contract balance of BCT */
        balance = IERC20(BCT).balanceOf(address(this));

    }

    function getBCTBalance() public view returns (uint bal) {

        /* return BCT balance */
        return balance;

    }

    function offsetBalanceOwner() onlyOwner public {
        
        _offsetBalance(balance, "#1UpCuban", "Cuban was not one-upped, but we made a difference!");

    }

    function changeTargetAmount(uint newTarget) onlyOwner public {

        targetAmount = newTarget;

    }

    function changeMinDeposit(uint newMinDeposit) onlyOwner public {

        minDeposit = newMinDeposit;

    }

    function _sendExtra() private {

        require(msg.sender == winners[CubanCount], "Not winner of current round - can't claim BCT changes");

        IERC20(BCT).transfer(msg.sender, balance);

        updateBCTBalance();
        
    }

    function _offsetBalance(uint offsetAmount, string memory beneficiary, string memory message) private {

        /* Retire the BCT */
        IERC20(BCT).approve(KlimaRetirementAggregator, offsetAmount);
        IKlimaRetirementAggregator(KlimaRetirementAggregator).retireCarbon(BCT, BCT, offsetAmount, false, msg.sender, beneficiary, message);
            
        updateBCTBalance();
        
    }

    

}