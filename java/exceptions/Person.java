public class Person {
	int age;
	String name;
	
	public Person(String name, int age)throws PersonException {
		if(age > 0) {
			this.age=age;
			this.name=name;
			System.out.println("You have created a person");
		}else {
			throw new PersonException("A person can't have a negative age:"+age);

		}
	}
	public void eat() {
		
	}
	public void walk() {
		
	}

}
