/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * 	@author Dhrumil Mistry
 * 	@github https://github.com/dmdhrumilmistry
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * 	Versions:
 * 		v1.0 
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *	
 * 	Methods:
 * 		GeneratePass():
 * 			returns character array 	
 * 			takes length of password as a parameter
 * 			Generates password using special characters, alphabets and numbers
 * 		
 * 		GeneratePassUsingNumbers():
 * 			returns character array 	
 * 			takes length of password as a parameter
 * 			Generates password using only numbers (0-9)
 * 
 * 		GeneratePassUsingUpperAlphabets():
 * 			returns character array 	
 * 			takes length of password as a parameter
 * 			Generates password using only Upper Alphabets (A-Z)
 * 		
 * 		GeneratePassUsingLowerAlphabets():
 * 			returns character array 	
 * 			takes length of password as a parameter
 * 			Generates password using only Lower Alphabets (a-z)
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

package dm.pass;

import java.util.Random;

public final class Generator {
	//Generates from all the Characters in ASCII Table
	public static char[] GeneratePass(int numberOfCharacters) {
		char[] pass = new char[numberOfCharacters];
		
		for(int i=0;i<numberOfCharacters;i++) 
			pass[i] = (char)(33 + (new Random()).nextInt(94)); 
		
		return pass;
	}
	
	public static char[] GeneratePassUsingNumbers(int numberOfCharacters) {
		char[] pass = new char[numberOfCharacters];
		
		for(int i=0; i<numberOfCharacters; i++)
			pass[i] = (char)(48 + (new Random().nextInt(9))); 
		
		return pass;
	}
	
	public static char[] GeneratePassUsingUpperAlphabets(int numberOfCharacters) {
		char[] pass = new char[numberOfCharacters];
		
		for(int i=0; i<numberOfCharacters; i++)
			pass[i] = (char)(65 + (new Random().nextInt(26))); 
		
		return pass;
	}
	
	public static char[] GeneratePassUsingLowerAlphabets(int numberOfCharacters) {
		char[] pass = new char[numberOfCharacters];
		
		for(int i=0; i<numberOfCharacters; i++)
			pass[i] = (char)(97 + (new Random().nextInt(26))); 
		
		return pass;
	}
	
}