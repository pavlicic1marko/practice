package oop;

public class Poziv extends Usluga {
	public int trajanje;
	
	public Poziv(Broj prvi,Broj drugi,int vreme) {
		super(prvi,drugi);
		this.trajanje=vreme;	
	}
	@Override
	public int cena() {
		int minutiRazgovora=(trajanje+59)/60;
		if(trajanje==0) {
			return 0;
		}
		if(this.inicirao.istaDrzava(upucena)) {
			return 0 + minutiRazgovora * 10;
		}
		else {
			return  30 + minutiRazgovora *50 ;
		}
		
		
	}
	@Override
	public String toString() {
		return super.toString() + " (" +trajanje/60 +":"+ trajanje%60 +")" ;
	}
}
