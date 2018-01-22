********************************************************************************************************************************
********************************************************************************************************************************
Authors : Guillaume Tochou & Raphael Neri
Grenoble INP - Phelma
********************************************************************************************************************************
********************************************************************************************************************************

Prerequisites
	
	Hardware : 	- 1 USRP
			- 1 RTL-SDR Dongle

	Software : 	- GNU Radio and dependencies: https://wiki.gnuradio.org/index.php/InstallingGR
			- gr-tutorial OOT : https://github.com/gnuradio/gr-tutorial.git
			- gr-osmosdr OOT : https://github.com/osmocom/gr-osmosdr.git

	Example commands to do for prerequisites :
	
		#GNU Radio
		$ cd $YOUR_DIRECTORY
		$ wget http://www.sbrac.org/files/build-gnuradio && chmod a+x build-gnuradio && ./build-gnuradio 

		#gr-tutorial
		$ cd $YOUR_DIRECTORY
		$ git clone https://github.com/gnuradio/gr-tutorial.git
		$ cd gr-tutorial/
		$ mkdir build
		$ cd build/
 		$ cmake ../
		$ make
		$ sudo make install
		$ sudo ldconfig
	
		#gr-osmosdr
		$ cd $YOUR_DIRECTORY
		$ git clone https://github.com/osmocom/gr-osmosdr.git
		$ cd gr-osmosdr/
		$ mkdir build
		$ cd build/
		$ cmake ../
		$ make
		$ sudo make install
		$ sudo ldconfig

	For any help please report to : https://wiki.gnuradio.org/index.php/Main_Page

********************************************************************************************************************************
********************************************************************************************************************************

How to Run Demonstration : 

	Transmitter : 	- Plug the USRP 
			- Run the following commands :
				$ usrp_find_devices 
				$ cd /$PROJECT_DIRECTORY/Transceiver/
				$ gnuradio-companion TX_USRP_file.grc &
			- In File Source block select the path of the file to sent ($PROJECT_DIRECTORY/TX_files/HelloWorld.txt for example)
			- Click on Generate to generate the python executable script
			- Click on Execute to run the transmitter 

	Receiver : 	- Plug the Dongle RTL-SDR 
			- Run the following commands :
				$ rtl_tcp #let the command running in a terminal
				$ cd /$PROJECT_DIRECTORY/Receiver/
				$ gnuradio-companion RX_rtl_file.grc &
			- In File Sink block enter the path of the received file ($PROJECT_DIRECTORY/RX_files/your_file.txt for example)
			- Click on Generate to generate the python executable script
			- Click on Execute to run the receiver  	
********************************************************************************************************************************
********************************************************************************************************************************
