import java.util.Random;
public class Dice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random dice = new Random();
		for (int counter=1; counter<10; counter++) {
			int number=dice.nextInt(6);
			System.out.println(number+1);
		}
		
	}

}
