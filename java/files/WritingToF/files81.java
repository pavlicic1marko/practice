import java.io.*; 
import java.util.*;
public class files81 {
	private Scanner  x;
	
	public void openFile() {
		try {
			x= new Scanner( new File("C:\\test\\Chinese.txt"));
		}
		catch(Exception e) {
			System.out.println("could not find the file");
		}
		
	}
	public void readFile() {
		while(x.hasNext()) {
			String a = x.next();
			String b = x.next();
			String c = x.next();
			System.out.printf("%s %s %S",a,b,c);
			System.out.print("\n");
		}
	}
	public void closeFile() {
		x.close();
	}
}
