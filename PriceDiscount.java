import java.util.Scanner;
  public class PriceDiscount {
  public static void main(String[] args) {

	Scanner keyz = new Scanner(System.in);
	System.out.println("Enter Price");
	float price = keyz.nextFloat();

	System.out.println("Enter Discount");
	float discount = keyz.nextFloat();

	float newPrice = price -((price * discount)/100);

	System.out.printf("The discounted price is: %.3f",newPrice);




}

}