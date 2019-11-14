#instale lynx,mininet e ettercap

mininet --topo=single,2 --nat #criar topologia com 2 nós com suporte a nat
xterm h1 h2
#no h2
ettercap -G #habilite modo promiscuo, setar mascara 255.255.255.0 , comecar arp poisoning nos remotos
#clicar em ver conecçoes
#no h1
lynx http://testing-ground.scraping.pro/login