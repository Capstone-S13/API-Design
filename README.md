# Link to Miro Board of API Design
https://miro.com/welcomeonboard/a3lmYXhPNEVWVHdQV0VGY3F0djdRWGdnbnZDb3ZaakpOV3Uxbk01U0VEOWRmNFJyR2gzWGJ5bGhLS21WcTFnUnwzMDc0NDU3MzUxNTMyNzUwOTI5?invite_link_id=453069555081
##### How does the robots in the RMF interact with each other? (waypoint thingy)
##### How does the robot know when to move to the HUB from the shop?
* when order comes in, notify vendor
* vendor accepts
* vendor notifies app when ready for collection
* deploy robot to store
* some prompt to notify robot order is in
* robot update status of item
* robot proceeds back to HUB to place it in HUB
* update on status of item
* notify external robot to collect
* external robot collects (accepting external robot into RMF to be done in another area)
* update on status of item
* transport to the other HUB
* update status again
* notify internal robot to collect from HUB
* internal collects from HUB
* brings to doorstep
* notify customer order has arrive.

#####Accepting External robot into the RMF instance
* Send external robot to mall when order is made(?)
* notify mall server when it arrives at the mall
* RMF fleet adapter accepts the external robot
* Direct it to HUB yada yada
* Fleet adapter removes the external robot
* RMF notifies the mall server that external robot is removed
* External robot goes back to its default system (ie another RMF instance maybe)

##### How does robot interact with the HUB?
* update API server on the status
* naming of different hub

##### Does each mall have their own database?
Yes

##### What is the format for address?
string/integer