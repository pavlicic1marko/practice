import java.io.File;
public class FileClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a=0;
		File x = new File("C:\\test\\greg.txt");
		if (x.exists()) {
			System.out.println("postoji");
			}
		else {
			System.out.println("ne  postoji");
		}
			
	
	}

}
