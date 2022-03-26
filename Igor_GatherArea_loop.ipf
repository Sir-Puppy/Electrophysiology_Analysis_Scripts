#pragma TextEncoding = "UTF-8"
#pragma rtGlobals=3				// Use modern global access method and strict wave access
#pragma version=9		// revised for Igor 9

//This function will loop through traces/waves until a limit set by the user. The variable number (a) is the number that changes between traces within a file

Function DoWhile(a) //Unsure why, but Igor requires an imput, rather than just a blank function. Just put any number as a, and it will be changed to 1 later
	variable a;
	
	
	
	string str1 = "root:W220210_2_E1_1_3_" //First hald of the wave name
	
	string str2 = "_1" //second half of wave name
	
	string together

	a = 1; //starting number
	

	do	
	
		together = str1 + num2str(a) + str2 //Stitch together the two halves plus variable to form the wave name in string format
		
		wave wr=$together //modify string into wave

		print area(wr, 0.1505, 0.2005) //prints area of wave between 0.1505 and 0.2005
	
				
		a += 1;
		
	while( a<23) //Loop limit
end
