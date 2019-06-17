public class Main{

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		bacteria[] newobject = new bacteria[2];
		salmonela object1 = new salmonela();
		streptococus object2 = new streptococus();
		newobject[0]=object1; 
		newobject[1]=object2; 
		for (bacteria x: newobject) {
			x.noise();
		}

	}

}
