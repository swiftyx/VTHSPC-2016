import java.util.Scanner;
import java.util.ArrayList;
public class Mia {
   public static int cal(int a, int b) {
      int max = Math.max(a,b);
      int min = Math.min(a,b);
      if (max == 2 && min == 1)
         return 400;
      else if (max == min)
         return (max * 10 + max) * 6;
      else
         return (max*10+min);
   }
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      ArrayList<String> r = new ArrayList<String>();
      while (in.hasNextInt()) {
         int a,b,c,d,aS,bS;
         a = in.nextInt();
         b = in.nextInt();
         c = in.nextInt();
         d = in.nextInt();
         if (a+b+c+d==0) break;
         aS = cal(a,b);
         bS = cal(c,d);
         if (aS > bS) {
            r.add("Player 1 wins.");
         } else if (aS < bS) {
            r.add("Player 2 wins.");
         } else {
            r.add("Tie.");
         }
      }
      for (int i=0;i<r.size();i++) {
         System.out.println(r.get(i));
      }
   }
}
