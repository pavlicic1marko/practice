public class Main_Threads {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread t1 = new Thread(new Bacon("one"));
		Thread t2 = new Thread(new Bacon("two"));
		Thread t3 = new Thread(new Bacon("three"));
		t1.start();
		t2.start();
		t3.start();
		

	}

}
