import java.util.*; 


public class Playing {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x=10;
		int i =0;
		int[] intArray = new int[11];
		
		while(x>i) {
			System.out.println(i);
			i++;
			intArray[i]=i;	
		}
		
		
		for (int value:intArray) {
			System.out.print(value+" ");
		}
		
		
		//int[][] TwoDimensionallArray = new int[2][];
		
		
		do {
			System.out.println("kako ste");
			}
		while (x>i);
		
		for (int value:intArray) {
			System.out.print(value+" ");
		}
		
		System.out.println();
		String stringVariable="Friday";
		switch(stringVariable) {
		case "Monday":
			System.out.println("it is Monday");
			break;
		case "Friday":
			System.out.println("it is Friday");
			break;
		default:
			System.out.println("it is i dont know");

		}
		ArrayList<String> MyList = new ArrayList<>();
		MyList.add("opala");
		MyList.add("xxxxxx");
		MyList.add("ananas");
		MyList.add("banana");
		Iterator<String> MyListIterator = MyList.iterator();
		
		while (MyListIterator.hasNext()) { 
            System.out.print(MyListIterator.next() + " ");
        } 
		String[] MyArray= {"as","dasd","dsfsd","fsdfs","sfdf"};
		List ObjectList = Arrays.asList(MyArray);
		
		System.out.println("\n"+ObjectList);
	}
	
		
}

