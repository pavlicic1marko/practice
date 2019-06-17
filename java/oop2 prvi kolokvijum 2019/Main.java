package oop;
import oop.Poruka;
import oop.Broj;
import oop.Usluga;
import oop.Korisnik2;

public class Main {

	public static void main(String[] args) {
		Broj b1 = new Broj("381","64","0000000",false);
		Broj b2 = new Broj("381","11","0000000",true);
		Broj b3 = new Broj("454","59","0000000",false);

		Poziv poziv1 = new Poziv(b1, b3, 253);
		Poruka poruka1 = new Poruka(b1, b3, "dobar dan");
		
		System.out.println(poziv1);
		System.out.println(poruka1);
		
		System.out.println();
		
		Korisnik2 k =new Korisnik2(b1, 2);
		k.evidentirajPoziv(b2,74);
		k.evidentirajPoruku(b3,"Zdravo");
		k.evidentirajPoruku(b3,"Cao");

		 System.out.println(k);
		 System.out.println("Ukupna cena: "+ k.ukupnaCena());
		
		

	}

}
