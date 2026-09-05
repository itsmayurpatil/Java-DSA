import java.util.Scanner;

public class Input {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("enter your name :");
        String name = sc.nextLine();      // nextLine() method is used to read the string input from the user.

        System.out.println("hello " + name + "!");

        sc.close();
    
    }
}
