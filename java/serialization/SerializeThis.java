// Java object for serialization and deserialization  

  
class SerializeThis implements java.io.Serializable 
{ 
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public int a; 
    public String b; 
    //without transient there would be an error,because in the constructor we set the c
    transient public ObjectClass c=null;
  
    // Default constructor 
    public  SerializeThis(int a, String b) 
    { 
        this.a = a; 
        this.b = b;
        SetC();
        
    } 
    public void SetC() {
        this.c = new ObjectClass();

    }
} 
