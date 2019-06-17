package oop;

public abstract class Usluga {
	public Broj inicirao;
	public Broj upucena;
	
	public Usluga(Broj inicirao, Broj upucena) {
		this.inicirao = inicirao;
		this.upucena = upucena;
	}


	public String toString(){
		return inicirao +" -> "+ upucena;
		
	}
	public abstract int cena();

}
