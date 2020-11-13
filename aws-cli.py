import os
import getpass

os.system("clear")
print("- - - - - - - - - - - - - - - - - -  ")
print("  _         _ _      _ _       _ _") 
print(" /_\  |  | (_ _  _  |     |     | ")
print("/   \ |/\|  _ _)    |_ _  |__  _|_")
print("- - - - - - - - - - - - - - - - - - -")
password=getpass.getpass("password : ")

if password != "redhat":
		print("Incorrect")
		exit()
	
	

os.system("tput setaf 6")
print("\t\t\t*WELCOME TO LINUXWORLD*\n\n")
os.system("tput setaf 2")
print("\tSo..How may we help you!!")
print("""
	Press 1 => To launch an Ec2 instance on AWS
	Press 2 => To create an EBS volume
	Press 3 => To attach that EBS volume
	press 4 => To create the S3 Bucket and make it public 
	press 5 => To copy file from your storage to S3 Bucket
	press 6 => To create Cloudfront Distribution
	press 7 => To exit 
	""")
os.system("tput setaf 7")
ch = input("Select your choice from the given options here: ")
if int(ch) == 1:
		
		#launching ec2 instance
		x=input("Please enter AMI:")
		y=input("Please enter your security group id:")
		z=input("Please enter your key for authentication:")
		s=input("Please enter the type of ec2-instance:")
		k=input("Please enter the count of instance:")
		os.system("aws ec2 run-instances --image-id{0} --security-group-ids{1} --key-name{2} --instance-type{3} --count{4}".format(x,y,z,s,k))

elif int(ch) == 2:
		#print("creating EBS volume")
		region=input("Enter the region :")
		size=input("Enter size of volume:")
		os.system("aws ec2 create-volume --volume -type gp2 --availability-zone {0} --size {1}".format(region,size))
		
		
elif int(ch) ==3:
		#print("attaching that EBS volume")
		vol=input("Enter volume id:")
		iid=input("Enter instance id:")
		dt=input("Enter device type:")
		os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}".format(vol,iid,dt))

elif int(ch) ==4:
		#print("create a s3 bucket and make public")
		bname = input("please enter your bucket name:")
		bregion= input("Please enter the region where u want to make your bucket: ")
		os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(bname,bregion))
		os.system("aws s3api put-bucket-acl --acl public-read --bucket {0}".format(bname))
		print("Successfully created Bucket {0} in {1} publickely".format(bname,bregion))

elif int(ch) ==5:
		#Uploading the file to s3
			path = input("enter the path of file : ")
			os.system("aws s3 cp {} s3://{}/{} --acl public-read".format(path,bname,path)) 
			print("File is successfully uploaded to s3 bucket from your storage.")

elif ch == 6:
		#Creating Cloudfront distribution
		Origin= input("Please enter the S3 bucket you want to make as origin for CDN: ")
		os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(Origin))
		print("Successfully created Content delivery network")

elif ch == 7:
		exit()

else:
		print("Please try again")

		


		










