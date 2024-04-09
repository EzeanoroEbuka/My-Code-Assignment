import java.util.Scanner;
  public class NaturaNumber {
   public static void main(String[] args) {

	Scanner keyz = new Scanner(System.in);

	int count = 0;
	int total = 0;	

	while(count < 10) {
	count++;
	System.out.println("Enter Number");
	int num = keyz.nextInt();
	total += num;
	}
	System.out.println("The sum of the digits is :" + total);

}


}