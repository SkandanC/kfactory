from typing import Callable, Dict, Tuple, Union

from pydantic import BaseModel

MaterialSpec = Union[str, float, Tuple[float, float], Callable]

material_name_to_lumerical: Dict[str, MaterialSpec] = {
    "si": "Si (Silicon) - Palik",
    "sio2": "SiO2 (Glass) - Palik",
    "sin": "Si3N4 (Silicon Nitride) - Phillip",
}


class SimulationSettingsLumericalFdtd(BaseModel):
    """Lumerical FDTD simulation_settings.

    Parameters:
        background_material: for the background.
        port_margin: on both sides of the port width (um).
        port_height: port height (um).
        port_extension: port extension (um).
        mesh_accuracy: 2 (1: coarse, 2: fine, 3: superfine).
        zmargin: for the FDTD region (um).
        ymargin: for the FDTD region (um).
        xmargin: for the FDTD region (um).
        wavelength_start: 1.2 (um).
        wavelength_stop: 1.6 (um).
        wavelength_points: 500.
        simulation_time: (s) related to max path length
            3e8/2.4*10e-12*1e6 = 1.25mm.
        simulation_temperature: in kelvin (default = 300).
        frequency_dependent_profile: compute mode profiles for each wavelength.
        field_profile_samples: number of wavelengths to compute field profile.
    """

    background_material: str = "sio2"
    port_margin: float = 1.5
    port_extension: float = 5.0
    mesh_accuracy: int = 2
    wavelength_start: float = 1.2
    wavelength_stop: float = 1.6
    wavelength_points: int = 500
    simulation_time: float = 10e-12
    simulation_temperature: float = 300
    frequency_dependent_profile: bool = True
    field_profile_samples: int = 15
    distance_monitors_to_pml: float = 0.5
    material_name_to_lumerical: Dict[str, MaterialSpec] = material_name_to_lumerical

    class Config:
        """pydantic basemodel config."""

        arbitrary_types_allowed = True


SIMULATION_SETTINGS_LUMERICAL_FDTD = SimulationSettingsLumericalFdtd()

if __name__ == "__main__":
    from kfactory.serialization import clean_value_json

    d = clean_value_json(SIMULATION_SETTINGS_LUMERICAL_FDTD)
