// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

import "../interfaces/IKlimaRetirementAggregator.sol";
import "../interfaces/IERC20.sol";

contract OneUpCuban {

    uint public minDeposit;
    uint public targetAmount;
    uint public balance;
    uint public CubanCount;
    
    address public immutable KlimaRetirementAggregator;
    address public immutable BCT;
    address public immutable owner; /*TESTING */

    mapping(uint => address) public winners;

    constructor(address _BCT) {

        KlimaRetirementAggregator = 0xEde3bd57a04960E6469B70B4863cE1c9d9363Cb8;
        /*BCT = 0x2F800Db0fdb5223b3C3f354886d907A671414A7F;*/ /* UNCOMMENT WHEN DEPLOYED TO MAINNET */
        BCT = _BCT; /* JUST FOR LOCAL TESTING */
        targetAmount =  101000000000000000000 ; /*101 BCT*/
        minDeposit =    1000000000000000000; /* 1 BCT */
        owner = msg.sender; /* JUST FOR LOCAL TESTING */
        
    }


    function deposit(uint amount) public {

        require(amount >= minDeposit, "Cannot deposit less than 1 BCT");
        require(IERC20(BCT).allowance(msg.sender, address(this)) >= amount, "Contract must have sufficient spending allowance of BCT amount");

        IERC20(BCT).transferFrom(msg.sender, address(this), amount);
        
        updateBCTBalance();

        if (balance >= targetAmount) {

            /* approve spend, and retire 101 BCT */
            /* winner is beneficiary */

            /* COMMENT OUT FOR LOCAL TESTING AND REPLACE WITH TRANSFER TO DEPLOYER */
            /*
            IERC20(BCT).approve(KlimaRetirementAggregator, targetAmount);
            IKlimaRetirementAggregator(KlimaRetirementAggregator).retireCarbon(BCT, BCT, targetAmount, true, msg.sender, "#1UpCuban", "Cuban was one-upped!");
            */
            
            IERC20(BCT).transfer(owner, targetAmount); /* JUST FOR LOCAL TESTING */

            updateBCTBalance();

            /* set winner send remaining change to winner */
            winners[CubanCount] = msg.sender;
            sendExtra();

        }

    }

    function sendExtra() private {

        require(msg.sender == winners[CubanCount], "Not winner of current round - can't claim dust");

        IERC20(BCT).transfer(msg.sender, balance);

        updateBCTBalance();

        /* Increment Cuban count */
        CubanCount++;
        
    }

    function updateBCTBalance() public {

        /* Update current contract balance of BCT */
        balance = IERC20(BCT).balanceOf(address(this));

    }

    function getBCTBalance() public view returns (uint bal) {

        /* return BCT balance */
        return balance;

    }

}