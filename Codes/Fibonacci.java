import java.util.Scanner;
import java.math.*;

public class Fibonacci {
  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    int a;
    System.out.println("How many steps?");
    a = in.nextInt();
    System.out.println("Fibonacci Numbers");
    BigInteger i = new BigInteger("1");
    BigInteger[] arr = new BigInteger[a];
    arr[0] = i;
    arr[1] = i;
    for (int h=0; h<2; h++){
      System.out.println("1");
    }
    
    for (int h =2; h<a-2 ; h++){
      arr[h] = arr[h-1].add(arr[h-2]);
      System.out.println(arr[h]);
    }
    System.out.println("\nAurean Number");
    for (int h = 1; h<a; h++){
      BigDecimal e1 = new BigDecimal(arr[h]);
      BigDecimal e2 = new BigDecimal(arr[h-1]);
      System.out.println(e1.divide(e2, 30, RoundingMode.CEILING));
    }
  }
}
