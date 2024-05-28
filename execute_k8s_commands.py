import paramiko

#Create ssh_client object in order to create connection with client
ssh_client=paramiko.SSHClient()

#Save client details in one variable
ssh_client_details={'hostname':'_._._._','username':' ','password':''}

#Set missing host key policy to avoid getting error of missing hostname
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#Create SSH connection with client
ssh_client.connect(**ssh_client_details)

try:
    if ssh_client.get_transport().is_active():
        stdin, stdout, stderr = ssh_client.exec_command('\nmicrok8s kubectl get pods --all-namespaces')
        output = stdout.read()
        output = output.decode()
        print(output)
    else:
        print("\nPlease check the connection towards ssh_client")

except Exception as err:
    print(err)

print(f'Done executing commands on SSH Client : {ssh_client_details["hostname"]},closing connection now!')
print('Bye,bye')
ssh_client.close()
