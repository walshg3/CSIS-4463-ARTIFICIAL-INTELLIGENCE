import csis4463.*;
import java.util.ArrayList;
import java.util.HashMap;

/**
 * For this assignment, you will need the puzzle.jar file and its documentation (docs.zip) 
 * from homework 4, and the Examples.java will be useful as well.
 *
 * In Java, implement any search algorithm that we saw in class to solve sliding tile
 * puzzles, such as the 8 puzzle, 15 puzzle, etc.
 *
 * You must not change the name, parameters, or return type of the solver method.
 * You are free to add as many helper methods as you find useful.
 *
 * You are free to use the MinHeapPQ class that is in the puzzle.jar (see its documentation).
 * It supports changing the priority of elements that are in the PQ, whereas the PQ implementation
 * in the Java API does not support that operation.
 *
 * Grading:
 * Your grade will be in the interval [0, 100] if you implement an algorithm that is guaranteed
 * to find the optimal path.  Otherwise, if you implement an algorithm that is not
 * guaranteed to find the optimal path (e.g., DFS), then your grade will be in the interval [0, 85]
 * (i.e., you lose 15 points for the non-optimal algorithms).
 *
 * If your code doesn't compile, then your grade will be in the interval [0, 60] depending upon the severity
 * of the syntax errors.  i.e., make sure your code compiles (you lose at least 40 points if it doesn't.
 *
 * After completing the solver method, write code to demonstrate that it works in the Homework5Main class.
 *
 * @author Brain Fox and Greg Walsh
 * ______      _              ______                          _   _____                  _    _       _     _     
 *  ___ \    (_)             |  ___|                        | | |  __ \                | |  | |     | |   | |    
 *| |_/ /_ __ _  __ _ _ __   | |_ _____  __   __ _ _ __   __| | | |  \/_ __ ___  __ _  | |  | | __ _| |___| |__  
 *| ___ \ '__| |/ _` | '_ \  |  _/ _ \ \/ /  / _` | '_ \ / _` | | | __| '__/ _ \/ _` | | |/\| |/ _` | / __| '_ \ 
 *| |_/ / |  | | (_| | | | | | || (_) >  <  | (_| | | | | (_| | | |_\ \ | |  __/ (_| | \  /\  / (_| | \__ \ | | |
 *\____/|_|  |_|\__,_|_| |_| \_| \___/_/\_\  \__,_|_| |_|\__,_|  \____/_|  \___|\__, |  \/  \/ \__,_|_|___/_| |_|
 *                                                                               __/ |                           
 *                                                                             |___/                            
 * Algorithm chosen: A* with Manhattan Distance as hueristic
 */
 /*
	Sudo Code:
		PQ.pop
		if isGoalState
			return path
		store HashValue in HT
	for each succesor 
		if in PQ or not in HT
			calculate priority
			push to PQ
 */
public class Homework5 {
	
	/**
	 * Solves sliding tile puzzles with the algorithm of your choice.
	 *
	 * @return A path from the start state to the goal state.
	 */
	public ArrayList<SlidingTilePuzzle> solver(SlidingTilePuzzle start) {
		// this return here temporarily so this compiles.

		// Create PQ and HashSet
		MinHeapPQ<SlidingTilePuzzleCurrent> PQ = new MinHeapPQ<>();
		HashMap<String,Integer> HS = new HashMap<>();
		
		SlidingTilePuzzleCurrent initial = new SlidingTilePuzzleCurrent(start);
		//PQ.pop
		PQ.offer(initial,0);
		while (!PQ.isEmpty()){
			//pop PQ
			SlidingTilePuzzleCurrent current = PQ.poll();
			//System.out.println(current);
			/*
			if isGoalState
			return path
			*/
			if (current.isGoalState()){
				return current.getPath();
			}
			//store HashValue in HT
			HS.put(current.getHashValue(),current.getPriority());
			/*
			for each succesor 
			if in PQ or not in HT
			calculate priority
			push to PQ
			*/
			for (SlidingTilePuzzleCurrent successor : current.getSuccessors()) {
				if (!HS.containsKey(successor.getHashValue())){				
					PQ.offer(successor,successor.getPriority());
				}else{
					if(successor.getPriority()<HS.get(successor.getHashValue())){
						HS.put(successor.getHashValue(),successor.getPriority());
						PQ.offer(successor,successor.getPriority());
					}
				}
			}
		}
		
		return null;



	}
}
