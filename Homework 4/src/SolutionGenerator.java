//Brian Fox and Greg Walsh
import java.util.ArrayList;
import csis4463.*;
public class SolutionGenerator {
	public static void main(String[] args) {
		ArrayList<ArrayList<Long>> totals;
		Table statesExpanded = new Table(7,6,"Number of States Expanded");
		Table statesGenerated = new Table(7,6,"Number of States Generated");
		Table statesInMemory = new Table(7,6,"Most Number of States In Memory");
		
		for(int path=2;path<13;path += 2) {
			//write path length to each of the three tables
			String strPath = new Integer(path).toString();
			statesExpanded.fill(strPath);
			statesGenerated.fill(strPath);
			statesInMemory.fill(strPath);
			
			//overwrite totals to store data for next path length
			totals = new ArrayList<>(18);
			for(int i=0;i<18;i++) {
				totals.add(new ArrayList<>(100));
			}
			/*
			 * data in totals :
			 *  0:ucs states expanded		 1:ucs states generated		 2:ucs states in memory
			 *  3:a*1 states expanded		 4:a*1 states generated		 5:a*1 states in memory
			 *  6:a*2 states expanded		 7:a*2 states generated		 8:a*2 states in memory
			 *  9:id states expanded		10:id states generated		11:id states in memory
			 * 12:ida*1 states expanded		13:ida*1 states generated	14:ida*1 states in memory
			 * 15:ida*2 states expanded		16:ida*2 states generated	17:ida*2 states in memory
			 * 
			 */
			
			for(int i=0;i<100;i++) {
				/*
				 * generate a puzzle with optimal path length of size path
				 * generate a solutions using each algorithm
				 * push data from solution into the corresponding list 
				 * for an 8 puzzle we need a 3,3 not 8,8 which was causing problems with runtime.
				 */
				SlidingTilePuzzle stp = new SlidingTilePuzzle(3,3,path);

				PuzzleSolution solution = SlidingTilePuzzleSolver.uniformCostSearch(stp);
				totals.get(0).add((long)solution.getNumberOfStatesExpanded());
				totals.get(1).add(solution.getNumGenerated());
				totals.get(2).add((long)solution.getNumberOfStatesInMemory());

				solution = SlidingTilePuzzleSolver.AStarSearchMisplacedTiles(stp);
				totals.get(3).add((long)solution.getNumberOfStatesExpanded());
				totals.get(4).add(solution.getNumGenerated());
				totals.get(5).add((long)solution.getNumberOfStatesInMemory());

				solution = SlidingTilePuzzleSolver.AStarSearchManhattanDistance(stp);
				totals.get(6).add((long)solution.getNumberOfStatesExpanded());
				totals.get(7).add(solution.getNumGenerated());
				totals.get(8).add((long)solution.getNumberOfStatesInMemory());

				solution = SlidingTilePuzzleSolver.iterativeDeepening(stp);
				totals.get(9).add((long)solution.getNumberOfStatesExpanded());
				totals.get(10).add(solution.getNumGenerated());
				totals.get(11).add((long)solution.getNumberOfStatesInMemory());

				solution = SlidingTilePuzzleSolver.idaStarMisplacedTiles(stp);
				totals.get(12).add((long)solution.getNumberOfStatesExpanded());
				totals.get(13).add(solution.getNumGenerated());
				totals.get(14).add((long)solution.getNumberOfStatesInMemory());

				solution = SlidingTilePuzzleSolver.idaStarManhattanDistance(stp);
				totals.get(15).add((long)solution.getNumberOfStatesExpanded());
				totals.get(16).add(solution.getNumGenerated());
				totals.get(17).add((long)solution.getNumberOfStatesInMemory());
			}

			for(int i=0;i<totals.size();i++) { //for each list
				long sum = 0;
				for(Long solutionData : totals.get(i)) { // for each peice of data
					sum += solutionData; //add to sum
				}

				//write average to table
				if(i%3==0)statesExpanded.fill(new Double(sum/100d).toString());
				else if(i%3==1)statesGenerated.fill(new Double(sum/100d).toString());
				else statesInMemory.fill(new Double(sum/100d).toString());
			}
		}
		
		String[] headings = { "L","UCS","A*1","A*2","ID","IDA*1","IDA*2"};
		statesExpanded.setHeadings(headings);
		statesGenerated.setHeadings(headings);
		statesInMemory.setHeadings(headings);
		
		System.out.print(statesExpanded);
		System.out.print(statesGenerated);
		System.out.print(statesInMemory);
	}
}
