/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * 	@author Dhrumil Mistry
 * 	@github https://github.com/dmdhrumilmistry
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * 	Versions:
 * 		v1.0 
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *	
 * Class:
 *  	ConsoleInterface	
 * Methods:
 * 		getSafePassBanner():
 * 			return type void
 * 			takes no parameter
 * 			Prints SAFE PASS Name Banner with Dhrumil Mistry name and Github Account link
 * 		
 * 		printPassSafe():
 * 			return type void
 * 			takes no parameter
 * 			Prints the Safe Pass Name depending on random number generated
 * 
 * 		printBorder():
 * 			return type void	
 * 			takes number of times symbol to be printed and symbol as parameter
 * 			Prints the Symbol n times
 * 		
 * 		printMenu():
 * 			return type void	
 * 			takes no parameter
 * 			Prints the Password Generator Menu
 * 
 * 		printPassword():
 * 			return type void
 * 			takes character array pass as parameter
 * 			Prints the passed character array
 * 		
 * 		startConsoleApplication():
 * 			return type void
 * 			takes no parameter
 * 			Prints the Password Generator Menu
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

package dm.pass;

import java.util.Random;
import java.util.Scanner;

public final class ConsoleInterface {
	
	static void getSafePassBanner() {
		
		printBorder(80, '=');
		
		printPassSafe();
		
		System.out.println();
		
		printBorder(80, '-');
		
		System.out.println("Safe Pass --|Generate Random Passwords|--");
		System.out.println("Written By Dhrumil Mistry");
		System.out.println("github: https://github.com/dmdhrumilmistry/");
		
		printBorder(80, '=');
	}
	
	static void printPassSafe() {

		switch (new Random().nextInt(6) + 1){
		
			case 1: 
				System.out.println("  #####     #    ####### #######    ######     #     #####   #####  ");
				System.out.println(" #     #   # #   #       #          #     #   # #   #     # #     # ");
				System.out.println(" #        #   #  #       #          #     #  #   #  #       #       ");
				System.out.println("  #####  #     # #####   #####      ######  #     #  #####   #####  ");
				System.out.println("       # ####### #       #          #       #######       #       # ");
				System.out.println(" #     # #     # #       #          #       #     # #     # #     # ");
				System.out.println("  #####  #     # #       #######    #       #     #  #####   #####  ");
				break;
			
			case 2:
				System.out.println(" ________  ________  ________ _______           ________  ________  ________   ________      ");
				String tString =   "|\\   ____\\|\\   __  \\|\\  _____\\\\  ___ \\         |\\   __  \\|\\   __  \\|\\   ____\\ |\\   ____\\     ";
				System.out.println(tString);
				System.out.println("\\ \\  \\___|\\ \\  \\|\\  \\ \\  \\__/\\ \\   __/|        \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\___|_\\ \\  \\___|_    ");
				System.out.println(" \\ \\_____  \\ \\   __  \\ \\   __\\\\ \\  \\_|/__       \\ \\   ____\\ \\   __  \\ \\_____  \\\\ \\_____  \\   ");
				System.out.println("  \\|____|\\  \\ \\  \\ \\  \\ \\  \\_| \\ \\  \\_|\\ \\       \\ \\  \\___|\\ \\  \\ \\  \\|____|\\  \\\\|____|\\  \\  ");
				System.out.println("    ____\\_\\  \\ \\__\\ \\__\\ \\__\\   \\ \\_______\\       \\ \\__\\    \\ \\__\\ \\__\\____\\_\\  \\ ____\\_\\  \\ ");
				System.out.println("   |\\_________\\|__|\\|__|\\|__|    \\|_______|        \\|__|     \\|__|\\|__|\\_________\\\\_________\\");
				System.out.println("   \\|_________|                                                       \\|_________\\|_________|");
				break;
				
			case 3:
				System.out.println();
				System.out.println("  __ _  ___ ___   __  _   __ __ ");
				System.out.println(" (  /_|(_  (_    /__)/_| (  (   ");
				System.out.println("__)(  |/   /__  /   (  |__)__)  ");
				System.out.println();
				break;
				
			case 4:
				System.out.println();
				System.out.println(".-.  .  .--.--  .-. .  .-..-.");
				System.out.println("`-. /_\\ |- |-   |-'/_\\ `-.`-.");
				System.out.println("`-''   ''  '--  ' '   '`-'`-'");
				break;
			
			case 5:
				System.out.println("    _             _______  _______    ______            _       _    ");
				System.out.println("   | |      /\\   (_______)(_______)  (_____ \\  /\\      | |     | |   ");
				System.out.println("    \\ \\    /  \\   _____    _____      _____) )/  \\      \\ \\     \\ \\  ");
				System.out.println("     \\ \\  / /\\ \\ |  ___)  |  ___)    |  ____// /\\ \\      \\ \\     \\ \\ ");
				System.out.println(" _____) )| |__| || |      | |_____   | |    | |__| | _____) )_____) )");
				System.out.println("(______/ |______||_|      |_______)  |_|    |______|(______/(______/ ");
				break;
			
			case 6:
				System.out.println("  .-')     ('-.                  ('-.           _ (`-.    ('-.      .-')     .-')    ");
				System.out.println(" ( OO ).  ( OO ).-.            _(  OO)         ( (OO  )  ( OO ).-. ( OO ).  ( OO ).  ");
				System.out.println("(_)---\\_) / . --. /   ,------.(,------.       _.`     \\  / . --. /(_)---\\_)(_)---\\_) ");
				System.out.println("/    _ |  | \\-.  \\ ('-| _.---' |  .---'      (__...--''  | \\-.  \\ /    _ | /    _ |  ");
				System.out.println("\\  :` `..-'-'  |  |(OO|(_\\     |  |           |  /  | |.-'-'  |  |\\  :` `. \\  :` `.  ");
				System.out.println(" '..`''.)\\| |_.'  |/  |  '--. (|  '--.        |  |_.' | \\| |_.'  | '..`''.) '..`''.) ");
				System.out.println(".-._)   \\ |  .-.  |\\_)|  .--'  |  .--'        |  .___.'  |  .-.  |.-._)   \\.-._)   \\ ");
				System.out.println("\\       / |  | |  |  \\|  |_)   |  `---.       |  |       |  | |  |\\       /\\       / ");
				System.out.println(" `-----'  `--' `--'   `--'     `------'       `--'       `--' `--' `-----'  `-----'  ");
				break;
			default:
			System.out.println("SAFE PASS");
		}
	}
	
	static void printBorder(int number, char symbol) {
		for(int i = 1; i <= number; i++)
			System.out.print(symbol);
		System.out.println();
	}
	
	static void printMenu() {
		System.out.println("Choose to Generate a Random Safe Password:");
		System.out.println("1.\tOnly Numbers (0-9)");
		System.out.println("2.\tOnly Lower Alphabets (a-z)");
		System.out.println("3.\tOnly Upper Alphabets (A-Z)");
		System.out.println("4.\tUsing All of the above + Special Characters");
	}
	
	static void printPassword (char[] pass) {
		for(char c: pass) {
			System.out.print(c);
		}
		System.out.println();
	}
	
	public static void startConsoleApplication() {
		
		getSafePassBanner();
		
		System.out.println("Enter the length(Number of Characters) of your password:");
		Scanner scanner = new Scanner(System.in);
		int length = scanner.nextInt();
		System.out.println();
		
		printMenu();
		System.out.println("Enter your choice >> ");
		int choice = scanner.nextInt();
		scanner.close();
		
		boolean isValid = false;
		
		char[] pass = {' '};
		switch(choice) {
			case 1:
				pass = Generator.GeneratePassUsingNumbers(length);
				isValid = true;
				break;
				
			case 2:
				pass = Generator.GeneratePassUsingLowerAlphabets(length);
				isValid = true;
				break;
			
			case 3:
				pass = Generator.GeneratePassUsingUpperAlphabets(length);
				isValid = true;
				break;
				
			case 4:
				pass = Generator.GeneratePass(length);
				isValid = true;
				break;
				
			default:
				System.err.println("Enter Valid Choice!!");
				
		}

		if(isValid) {
			System.out.println();
			System.out.println("Generated Password: " );
			printPassword(pass);
		}
		
	}
}
