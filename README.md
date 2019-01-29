# upgraded-doodle
Main.tf -> Actual code to launch the web cluster
Variabes.tf -> File holds the variables to reference in the Main.tf
Userdatascript -> File holds the user data script, that's been referenced in the Main.tf
output.tf -> Prints the ELB DNS name and ELB Zone Id
we used teraform to create the infrastructure
 ASG and ELB
 And route 53
In the userscript we are actually copying static html
