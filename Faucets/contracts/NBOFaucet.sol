// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.4;

import "./WhitelistFaucet.sol";
import "../interfaces/IERC20.sol";

contract NBOFaucet is WhitelistFaucet {
    
    // The underlying token of the Faucet
    IERC20 token;
    
    // For rate limiting
    mapping(address=>uint256) nextRequestAt;
    
    // No.of tokens to send when requested
    uint256 faucetDripAmount = 1;

    // Default ERC20 decimals
    uint tokendecimals = 18;
    
    // Sets the address the underlying token
    constructor (address _TokenAddress, uint _decimals) {
        token = IERC20(_TokenAddress);
        tokendecimals = _decimals;
    }   
    
    // Sends the amount of token to the caller.
    function send() external isWhitelisted(msg.sender) {
        require(token.balanceOf(address(this)) > 1,"FaucetError: Empty");
        require(nextRequestAt[msg.sender] < block.timestamp, "FaucetError: Try again later");
        
        // Next request from the address can be made only after 5 minutes         
        nextRequestAt[msg.sender] = block.timestamp + (5 minutes); 
        
        token.transfer(msg.sender, faucetDripAmount * 10**tokendecimals);
    }  
    
    // Updates the underlying token address
     function setTokenAddress(address _tokenAddr) external onlyOwner {
        token = IERC20(_tokenAddr);
    }    
    
    // Updates the drip rate
     function setFaucetDripAmount(uint256 _amount) external onlyOwner {
        faucetDripAmount = _amount;
    }  

    // Updates the underlying token decimal number
     function setTokenDecimals(uint _decimals) external onlyOwner {
        tokendecimals = _decimals;
    }    
     
     // Allows the owner to withdraw tokens from the contract.
     function withdrawTokens(address _receiver, uint256 _amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= _amount,"FaucetError: Insufficient funds");
        token.transfer(_receiver, _amount);
    }    
}