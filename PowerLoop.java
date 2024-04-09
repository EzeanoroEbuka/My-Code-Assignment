import java.util.Scanner;
  public class PowerLoop {
   public static void main(String[] args) {
	Scanner keyz = new Scanner(System.in);
	
	int count = 0;
	int total = 0;
	System.out.println("Enter Base Number");
	int base = keyz.nextInt();
	
	System.out.println("Enter The Power Number");
	int power = keyz.nextInt();

	while(power > count) {
	count++;
	 total = (base * base);
	}
 	
	System.out.println(total);

}



}
	