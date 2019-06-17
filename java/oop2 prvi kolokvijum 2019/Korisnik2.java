package oop;

public class Korisnik2 {
	int arrayPointer;
	int brusluga;
	Broj brKorisnika;
	Usluga[] uslugaarray;
	
	public Korisnik2(Broj brojarg,int intarg) {
		brusluga=intarg;
		uslugaarray= new Usluga[brusluga];
		arrayPointer=0;
		brKorisnika=brojarg;
		System.out.println(brojarg);
	}
	public void evidentirajPoruku(Broj brojarg, String stringarg) {
		uslugaarray[arrayPointer]=new Poruka(this.brKorisnika,brojarg, stringarg);
		arrayPointer++;
		if(arrayPointer==uslugaarray.length) {
			expandarray();
		}
	}
	public void evidentirajPoziv(Broj brojarg, int minuti) {
		uslugaarray[arrayPointer]=new Poziv(this.brKorisnika,brojarg, minuti);
		arrayPointer++;
		if(arrayPointer==uslugaarray.length) {
			expandarray();
		}
	}
	public void expandarray() {
		Usluga[] tempArray= new Usluga[arrayPointer+10];
		for(int i =0;i<uslugaarray.length;i++) {
			tempArray[i]=uslugaarray[i];
		}
		uslugaarray=tempArray;
		
	}
	public  void printArray() {
		for (int i=0; i < arrayPointer; i++) {
		    System.out.println(uslugaarray[i].toString());
		}
	}
	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append(brKorisnika);
		sb.append("\n");
		for(int i =0;i<arrayPointer;i++) {
			sb.append(uslugaarray[i]);
			sb.append("\n");
		}
		return sb.toString();
	}
	public String ukupnaCena() {
		int sum=0;
		for(int i =0;i<arrayPointer;i++) {
			sum=sum+uslugaarray[i].cena();
		}
		String str = Integer.toString(sum);
		return str;
		
	}
}

