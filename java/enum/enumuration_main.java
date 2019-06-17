public class enumuration_main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(enumuration people: enumuration.values())
			System.out.printf("%s\t%s\t%s\n", people, people.getDesc() ,people.getYear());
		

	}

}
