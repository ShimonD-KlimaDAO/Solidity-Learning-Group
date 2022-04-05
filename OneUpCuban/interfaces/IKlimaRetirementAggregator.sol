
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

interface IKlimaRetirementAggregator {
    function retireCarbon(address _sourceToken,address _poolToken,uint256 _amount,bool _amountInCarbon,address _beneficiaryAddress,string memory _beneficiaryString,string memory _retirementMessage) external;
}