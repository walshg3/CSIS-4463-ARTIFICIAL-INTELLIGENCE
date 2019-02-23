import csis4463.*;

/**
 * See comments in Homework5.java first.
 * 
 * @author Your Name Goes here.
 */
public class Homework5Main {
	
	public static void main(String[] args) {
		// write code here to demonstrate that your 8 puzzle solver works.
		SlidingTilePuzzle stp = new SlidingTilePuzzle(3,3,7);
		Homework5 test = new Homework5();
		//test.solver(stp);
		for ( SlidingTilePuzzle path : test.solver(stp)) {
			System.out.println(path.toString());
		}
	}
}
