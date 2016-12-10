import java.util.Scanner;
import java.util.ArrayList;
public class Add {
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      ArrayList<Integer> r = new ArrayList<Integer>();
      while (in.hasNextInt()) {
         int a = in.nextInt();
         int b = in.nextInt();
         if (a==0&&b==0) break;
         r.add(a+b);
      }
      for (int i=0;i<r.size();i++) {
         System.out.println(r.get(i));
      }
   }
}
