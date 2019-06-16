public class Recursion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num1=4;
		int value;
		value=factorial(num1);
		System.out.println(value);
	}
	public static int factorial(int number) {
		if(number==1) {
			return 1;
		}
		return number * factorial(number-1);
		
	}
	
	
}
