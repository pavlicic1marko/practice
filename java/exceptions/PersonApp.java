public class PersonApp {

	public static void main(String[] args) {
		Person objectPerson= null;
		try {
			objectPerson= new Person("Natalia",-10);
			
		}
		catch(PersonException e){
			System.out.println(e.getMessage());
		}
	}

}
