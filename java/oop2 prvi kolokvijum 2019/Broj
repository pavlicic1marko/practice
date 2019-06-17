package oop;

public class Broj {
	private String kodDrzave, pozivniBroj, brojTelefona;
	private boolean indikator;
	
	public Broj(String kodDrzave,String pozivniBroj,String brojTelefona,boolean indikator) {
		this.brojTelefona=brojTelefona;
		this.indikator=indikator;
		this.kodDrzave=kodDrzave;
		this.pozivniBroj=pozivniBroj;
	
		
	}
	public boolean istaDrzava(Broj br) {
		return this.kodDrzave.equals(br.kodDrzave);
	}
	public String getPozivniBroj() {
		return  this.pozivniBroj;
	}
	public boolean daLiJe011() {
		return indikator;
	}
	public String toString() {
		return "+"+kodDrzave+" "+pozivniBroj+" "+brojTelefona;
	}
}

