# 代码生成时间: 2025-09-30 22:10:49
import numpy as np

"""
Clinical Trial Management System

This program is designed to manage clinical trials using Python and Numpy.
It includes features to add, update, and retrieve trial data.
"""

class ClinicalTrial:
    """Class to represent a clinical trial."""
    def __init__(self, trial_id, name, phase, status):
        self.trial_id = trial_id  # Unique identifier for the trial
        self.name = name        # Name of the trial
        self.phase = phase      # Trial phase (e.g., 1, 2, 3)
        self.status = status    # Trial status (e.g., 'ongoing', 'completed', 'paused')

    def __str__(self):
        return f"Trial ID: {self.trial_id}, Name: {self.name}, Phase: {self.phase}, Status: {self.status}"

    def update_status(self, new_status):
        """Update the trial's status."""
        self.status = new_status

    def update_phase(self, new_phase):
        """Update the trial's phase."""
        if 1 <= new_phase <= 3:
            self.phase = new_phase
        else:
            raise ValueError("Phase must be between 1 and 3")

class TrialManager:
    """Class to manage a collection of clinical trials."""
    def __init__(self):
        self.trials = []  # List to store all trials

    def add_trial(self, trial):
        """Add a new trial to the manager."""
        if not isinstance(trial, ClinicalTrial):
            raise TypeError("Only ClinicalTrial instances can be added")
        self.trials.append(trial)

    def get_trial(self, trial_id):
        """Retrieve a trial by its ID."""
        for trial in self.trials:
            if trial.trial_id == trial_id:
                return trial
        raise ValueError(f"Trial with ID {trial_id} not found")

    def update_trial_status(self, trial_id, new_status):
        """Update the status of a trial."""
        trial = self.get_trial(trial_id)
        trial.update_status(new_status)

    def update_trial_phase(self, trial_id, new_phase):
        """Update the phase of a trial."""
        trial = self.get_trial(trial_id)
        try:
            trial.update_phase(new_phase)
        except ValueError as e:
            raise ValueError(f"Error updating trial {trial_id}: {e}")

    def list_trials(self):
        """List all trials managed by the system."""
        for trial in self.trials:
            print(trial)

# Example usage:
if __name__ == "__main__":
    manager = TrialManager()
    try:
        # Create a new trial
        trial1 = ClinicalTrial(1, "Trial A", 1, "ongoing")
        manager.add_trial(trial1)
        
        # Update trial status
        manager.update_trial_status(1, "paused")
        
        # Update trial phase
        manager.update_trial_phase(1, 2)
        
        # List all trials
        manager.list_trials()
    except Exception as e:
        print(f"An error occurred: {e}")