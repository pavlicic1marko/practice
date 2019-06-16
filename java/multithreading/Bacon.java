import java.util.Random;

public class Bacon implements Runnable{
	String name;
	int time;
	Random r =new Random();
	
	public Bacon(String s) {
		name = s;
		time =r.nextInt(99);
		
	}
	public void run() {
		try {
			//System.out.printf("%s will sleap for %d\n",name,time);
			for(int i =0;i<1555;i++) {
				System.out.printf("%s is threading\n",name);
			}
			Thread.sleep(time);
			System.out.printf("%s is done",name);
		}catch(Exception e) {
			System.out.printf("ther was an error with %s ",name);
		}

	}
}
