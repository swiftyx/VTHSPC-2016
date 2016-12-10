import java.util.ArrayList;
import java.util.Scanner;
public class ColorNode {
   public ArrayList<ColorNode> connected = new ArrayList<ColorNode>();
   public int colorsNeeded;

   public ColorNode(){}

   public void add(ColorNode c) {
      connected.add(c);
   }

   public int cal() {

   }

   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      ColorNode[] vertices = new ColorNode[11];
      int n = in.nextInt();
      for (int i=0;i<n;i++) {
         vertices[i] = new ColorNode()
      }
      for (int i=0;i<n;i++) {
         String[] sn = in.nextLine().split(" ");
         for (int j=0;j<sn.length;j++) {
            int num = Integer.parseInt(sn[j]);
            vertices[i].add(vertices[num]);
         }
      }
      int max = 2;
      for (int i=0;i<n;i++) {
         max = Math.max(max,vertices[i].cal());
      }
      System.out.println(max);
   }
}
