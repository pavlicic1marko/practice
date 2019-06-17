import java.io.*;
import java.lang.*;
import java.util.*;

public class files80 {
	private Formatter x;
	
	public void openFile() {
		try {
			x = new Formatter("C:\\test\\chinese.txt");
		}
		catch(Exception e) {
			System.out.println("you have an error");
		}	
	}
	
	public void addRecords(){
		x.format("eee");
	
	}
	public void closefile(){
		x.close();
	}
}
