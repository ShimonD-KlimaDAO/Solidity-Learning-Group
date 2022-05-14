Talk about why use the pattern "transparent upgradeable proxy" which puts a "wall" between admin and user. 
Talk about 4 byte collisions and show how it is avoided with _fallback in ERC1967Proxy

Show the design image

Admin can ONLY call admin functions, and user can ONLY call implementation functions - no ambiguity


Show box, boxv2, and the code to deploy and upgrade.

1. https://mumbai.polygonscan.com/address/0x1F7a731303691c30eDdA9a01F29961BEF2919865#code
 	The upgrading proxy contract that points to the logic contract
 2. (1) is the same as Cujo's retirement aggregator! 
 	https://polygonscan.com/address/0xEde3bd57a04960E6469B70B4863cE1c9d9363Cb8#code
 3. transaction calling increment() in boxv2: 
 	https://mumbai.polygonscan.com/tx/0x1686c08802b77fe1681611d43b7381663a4ec5a11094a621409e7017df915b18
   it calls the contract from (1)! and a function that didn't exist in box v1 !
   
   
   
   
proxyadmin : (smart contract) account controlling 'proxy'
proxy: "top level" contract that the frontend, etc, point to - never changes. This is TransparentUpgradeableProxy
implementation: the contract that contains the logic. Can redeploy new 'implementation' and change address proxy points to.


Finally: bonus - your proxyadmin can be owned by a gnosis multisig! This is the "gold standard" of safety for upgradeable contracts, and KlimaDAO uses it.


Open tabs, in order:
https://docs.openzeppelin.com/contracts/3.x/api/proxy#TransparentUpgradeableProxy
https://blog.openzeppelin.com/the-transparent-proxy-pattern/
https://docs.openzeppelin.com/contracts/4.x/api/proxy#Proxy
https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master/contracts/proxy
	-- showed both erc1967 and proxy.sol to find fallback()
https://blog.trailofbits.com/2018/09/05/contract-upgrade-anti-patterns/
(proxy on mumbai) https://mumbai.polygonscan.com/address/0x1F7a731303691c30eDdA9a01F29961BEF2919865#code
(retirement agg proxy - same code) https://polygonscan.com/address/0xEde3bd57a04960E6469B70B4863cE1c9d9363Cb8
(final boxv2 increment transaction) https://mumbai.polygonscan.com/tx/0x1686c08802b77fe1681611d43b7381663a4ec5a11094a621409e7017df915b18
https://eth-brownie.readthedocs.io/en/stable/api-network.html?highlight=from_abi#Contract.from_abi
https://help.gnosis-safe.io/en/articles/3876461-create-a-safe
https://docs.openzeppelin.com/contracts/4.x/api/proxy#ERC1967Proxy


