package oop;

public class Poruka extends Usluga{
	String tekstPoruke;
	public Poruka(Broj inicirao, Broj upucena, String tekstPoruke) {
		super(inicirao, upucena);
		this.tekstPoruke=tekstPoruke;
	}
	public boolean daLiJePoslata() {
		if(inicirao.daLiJe011()==true || upucena.daLiJe011()==true) {
			return false;
		}else {
			return true;
		}
	}
	
	@Override
	public String toString(){
		return super.toString() +" "+ tekstPoruke;
	}
	@Override
	public int cena(){
		if(! this.daLiJePoslata()) {
			return 0;
		}else {
			if(inicirao.istaDrzava(upucena)) {
				return 3;
			}else {
				return 20;
			}
		}
	}
	

}
