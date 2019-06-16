import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashSet;
import java.util.Scanner;
import java.util.Set;

public class SortInput {

	public static void main(String[] args)
    {
        ArrayList java_array = new ArrayList(); //array list je poprilicno mocan, zato koristim njega + ima toString() koji sam ispisuje ceo niz
        while (true)
        {
            Scanner user_input = new Scanner(System.in);
            if(user_input.hasNextInt()){
                java_array.add(Integer.parseInt(user_input.next())); // user_input.next uzima string, e onda mi taj string konvertujemo u int i problem resen
            }
            else if(user_input.hasNext("ULAZNO")){
                Collections.sort(java_array); //built in funkcionalnost ArrayList-a i svih ostalih tipova izvedenih iz Set
                Set<String> s = new LinkedHashSet<>(java_array);// da bi obrisao duplikate uradi konverziju u hash mapu
                System.out.print(s.toString());
                break;
            }
            else if(user_input.hasNext("NIZLAZNO")){
                Collections.sort(java_array,Collections.reverseOrder());
                Set<String> s = new LinkedHashSet<>(java_array);
                System.out.print(s.toString());
                break;
            }
            else if(user_input.hasNext("NESORTIRANO")){
                System.out.print(java_array.toString());
                break;
            }
            else {
                System.out.println("morate da upisete prirodan broj!");
            }

        }
    }
}
