import java.util.Scanner;

public class problem2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the radius of circle :");
        double Radius = sc.nextDouble();

        System.out.println("Radius = " + (Radius));
        System.out.println("Area = " + (2* Radius));
        sc.close();
    }  
}
