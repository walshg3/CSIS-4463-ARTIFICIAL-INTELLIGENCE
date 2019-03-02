import csis4463.*;
import java.util.ArrayList;
/*
 * @author Brain Fox and Greg Walsh
 * ______      _              ______                          _   _____                  _    _       _     _     
 *  ___ \    (_)             |  ___|                        | | |  __ \                | |  | |     | |   | |    
 *| |_/ /_ __ _  __ _ _ __   | |_ _____  __   __ _ _ __   __| | | |  \/_ __ ___  __ _  | |  | | __ _| |___| |__  
 *| ___ \ '__| |/ _` | '_ \  |  _/ _ \ \/ /  / _` | '_ \ / _` | | | __| '__/ _ \/ _` | | |/\| |/ _` | / __| '_ \ 
 *| |_/ / |  | | (_| | | | | | || (_) >  <  | (_| | | | | (_| | | |_\ \ | |  __/ (_| | \  /\  / (_| | \__ \ | | |
 *\____/|_|  |_|\__,_|_| |_| \_| \___/_/\_\  \__,_|_| |_|\__,_|  \____/_|  \___|\__, |  \/  \/ \__,_|_|___/_| |_|
 *                                                                               __/ |                           
 *                                                                              |___/                            
 *
 */
public class Homework5Main {
	
	public static void main(String[] args) {
		// write code here to demonstrate that your 8 puzzle solver works.
		SlidingTilePuzzle stp;
		Homework5 test = new Homework5();
		//test.solver(stp);
		/*
		for ( SlidingTilePuzzle path : test.solver(stp)) {
			System.out.println(path.toString());
		}
		*/

		for(int i=1;i<32;i++){
			stp = new SlidingTilePuzzle(3,3,i);
			ArrayList<SlidingTilePuzzle> path = test.solver(stp);
			//check if the last state in path is the goal state
			//and if the path length is the same as the optimal path length
			//this will run a 3,3 puzzle for iterations from 1-31 to prove the path works
			//for optimal path lengths 
			if(path.size() != i+1 || !path.get(i).isGoalState()){
				System.out.println("FAILED");
			}
		}
		System.out.println("PASSED");
	}
}
