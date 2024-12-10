import unreal
from typing import Optional, Union

class LayeredMaterialLibrary:
    """
    Python wrapper for the AdvancedMaterialEditingLibrary plugin functionality.
    Provides methods for manipulating layered materials and their parameters.
    """

    # Channel mask constants
    CHANNEL_RED = unreal.LinearColor(1, 0, 0, 0)
    CHANNEL_GREEN = unreal.LinearColor(0, 1, 0, 0)
    CHANNEL_BLUE = unreal.LinearColor(0, 0, 1, 0)
    CHANNEL_ALPHA = unreal.LinearColor(0, 0, 0, 1)
    CHANNELS = [CHANNEL_RED, CHANNEL_GREEN, CHANNEL_BLUE, CHANNEL_ALPHA]

    @staticmethod
    def get_layer_count(instance: 'unreal.MaterialInstance') -> int:
        """
        Get the number of layers in a material instance.

        Args:
            instance (unreal.MaterialInstance): The material instance to check

        Returns:
            int: Number of layers in the material instance. Returns 0 if instance is invalid.
        """
        return unreal.LayeredMaterialLibrary.get_layer_count(instance)

    @staticmethod
    def add_material_layer(instance: 'unreal.MaterialInstance') -> bool:
        """
        Add a new material layer and corresponding blend layer to the material instance.

        Args:
            instance (unreal.MaterialInstance): The material instance to modify

        Returns:
            bool: True if the layer was successfully added, False otherwise
        """
        return unreal.LayeredMaterialLibrary.add_material_layer(instance)

    @staticmethod
    def is_layered_material(instance: 'unreal.MaterialInstance') -> bool:
        """
        Check if a material instance is a layered material.

        Args:
            instance (unreal.MaterialInstance): The material instance to check

        Returns:
            bool: True if the material is a layered material, False otherwise
        """
        return unreal.LayeredMaterialLibrary.is_layered_material(instance)

    @staticmethod
    def assign_layer_material(
        instance: 'unreal.MaterialInstance',
        layer_index: int,
        new_layer_function: 'unreal.MaterialFunctionInterface'
    ) -> bool:
        """
        Assign a material function to a specific layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to modify
            layer_index (int): Index of the layer to modify. Layer 0 is the base layer.
            new_layer_function (unreal.MaterialFunctionInterface): The material function to assign

        Returns:
            bool: True if the assignment was successful, False otherwise
        """
        return unreal.LayeredMaterialLibrary.assign_layer_material(instance, layer_index, new_layer_function)

    @staticmethod
    def assign_blend_layer(
        instance: 'unreal.MaterialInstance',
        layer_index: int,
        new_blend_layer_function: 'unreal.MaterialFunctionInterface'
    ) -> bool:
        """
        Assign a blend function to a specific layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to modify
            layer_index (int): Index of the layer. Note: internally offset by 1 from UI (layer 0 has no blend)
            new_blend_layer_function (unreal.MaterialFunctionInterface): The blend function to assign

        Returns:
            bool: True if the assignment was successful, False otherwise
        """
        return unreal.LayeredMaterialLibrary.assign_blend_layer(instance, layer_index, new_blend_layer_function)

    @staticmethod
    def get_layered_material_scalar_parameter_value(
        instance: 'unreal.MaterialInstance',
        parameter_name: str,
        layer_index: int
    ) -> float:
        """
        Get the value of a scalar parameter from a specific layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the layer containing the parameter

        Returns:
            float: The parameter value. Returns 0.0 if parameter not found or instance is invalid.
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_scalar_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_scalar_parameter_value(
        instance: 'unreal.MaterialInstanceConstant',
        parameter_name: str,
        layer_index: int,
        value: float
    ) -> bool:
        """
        Set the value of a scalar parameter in a specific layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the layer containing the parameter
            value (float): New value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_scalar_parameter_value(instance, parameter_name, layer_index, value)

    @staticmethod
    def get_layered_material_vector_parameter_value(instance: 'unreal.MaterialInstance',
                                                    parameter_name: str, layer_index: int) -> 'unreal.LinearColor':
        """
        Get the value of a vector parameter from a specific layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the layer containing the parameter

        Returns:
            unreal.LinearColor: The parameter value. Returns (0,0,0,0) if parameter not found or instance is invalid
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_vector_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_vector_parameter_value(instance: 'unreal.MaterialInstanceConstant',
                                                    parameter_name: str, layer_index: int,
                                                    value: 'unreal.LinearColor') -> bool:
        """
        Set the value of a vector parameter in a specific layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the layer containing the parameter
            value (unreal.LinearColor): New value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_vector_parameter_value(instance, parameter_name, layer_index, value)

    @staticmethod
    def get_layered_material_static_switch_parameter_value(
        instance: 'unreal.MaterialInstance',
        parameter_name: str,
        layer_index: int
    ) -> bool:
        """
        Get the value of a static switch parameter from a specific layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the layer containing the parameter

        Returns:
            bool: The parameter value. Returns False if parameter not found or instance is invalid.
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_static_switch_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_static_switch_parameter_value(
        instance: 'unreal.MaterialInstanceConstant',
        parameter_name: str,
        layer_index: int,
        value: bool
    ) -> bool:
        """
        Set the value of a static switch parameter in a specific layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the layer containing the parameter
            value (bool): New value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_static_switch_parameter_value(instance, parameter_name, layer_index, value)

    @staticmethod
    def get_layered_material_texture_parameter_value(
        instance: 'unreal.MaterialInstance',
        parameter_name: str,
        layer_index: int
    ) -> Optional['unreal.Texture']:
        """
        Get the value of a texture parameter from a specific layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the layer containing the parameter

        Returns:
            Optional[unreal.Texture]: The texture parameter value. Returns None if parameter not found or instance is invalid.
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_texture_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_texture_parameter_value(
        instance: 'unreal.MaterialInstanceConstant',
        parameter_name: str,
        layer_index: int,
        value: 'unreal.Texture'
    ) -> bool:
        """
        Set the value of a texture parameter in a specific layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the layer containing the parameter
            value (unreal.Texture): New texture value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_texture_parameter_value(instance, parameter_name, layer_index, value)

    @staticmethod
    def get_layered_material_channel_mask_parameter_value(instance: 'unreal.MaterialInstance',
                                                        parameter_name: str,
                                                        layer_index: int) -> 'unreal.LinearColor':
        """
        Get the value of a channel mask parameter from a specific layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the layer containing the parameter

        Returns:
            unreal.LinearColor: The parameter value. Returns (0,0,0,0) if parameter not found or instance is invalid
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_channel_mask_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_channel_mask_parameter_value(instance: 'unreal.MaterialInstanceConstant',
                                                        parameter_name: str,
                                                        layer_index: int,
                                                        value: 'unreal.LinearColor') -> bool:
        """
        Set the value of a channel mask parameter in a specific layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the layer containing the parameter
            value (unreal.LinearColor): New value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_channel_mask_parameter_value(instance, parameter_name, layer_index, value)


    # Blend Layer Parameters
    @staticmethod
    def get_layered_material_blend_scalar_parameter_value(instance: 'unreal.MaterialInstance',
                                                        parameter_name: str, layer_index: int) -> float:
        """
        Get the value of a scalar parameter from a specific blend layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the blend layer containing the parameter

        Returns:
            float: The parameter value. Returns 0.0 if parameter not found or instance is invalid
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_blend_scalar_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_blend_scalar_parameter_value(instance: 'unreal.MaterialInstanceConstant',
                                                        parameter_name: str, layer_index: int, value: float) -> bool:
        """
        Set the value of a scalar parameter in a specific blend layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the blend layer containing the parameter
            value (float): New value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_blend_scalar_parameter_value(instance, parameter_name, layer_index, value)

    @staticmethod
    def get_layered_material_blend_vector_parameter_value(instance: 'unreal.MaterialInstance',
                                                        parameter_name: str, layer_index: int) -> 'unreal.LinearColor':
        """
        Get the value of a vector parameter from a specific blend layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the blend layer containing the parameter

        Returns:
            unreal.LinearColor: The parameter value. Returns (0,0,0,0) if parameter not found or instance is invalid
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_blend_vector_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_blend_vector_parameter_value(instance: 'unreal.MaterialInstanceConstant',
                                                        parameter_name: str, layer_index: int,
                                                        value: 'unreal.LinearColor') -> bool:
        """
        Set the value of a vector parameter in a specific blend layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the blend layer containing the parameter
            value (unreal.LinearColor): New value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_blend_vector_parameter_value(instance, parameter_name, layer_index, value)

    @staticmethod
    def get_layered_material_blend_static_switch_parameter_value(instance: 'unreal.MaterialInstance',
                                                                parameter_name: str, layer_index: int) -> bool:
        """
        Get the value of a static switch parameter from a specific blend layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the blend layer containing the parameter

        Returns:
            bool: The parameter value. Returns False if parameter not found or instance is invalid
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_blend_static_switch_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_blend_static_switch_parameter_value(instance: 'unreal.MaterialInstanceConstant',
                                                                parameter_name: str, layer_index: int, value: bool) -> bool:
        """
        Set the value of a static switch parameter in a specific blend layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the blend layer containing the parameter
            value (bool): New value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_blend_static_switch_parameter_value(instance, parameter_name, layer_index, value)

    @staticmethod
    def get_layered_material_blend_texture_parameter_value(instance: 'unreal.MaterialInstance',
                                                        parameter_name: str, layer_index: int) -> Optional['unreal.Texture']:
        """
        Get the value of a texture parameter from a specific blend layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the blend layer containing the parameter

        Returns:
            Optional[unreal.Texture]: The texture parameter value. Returns None if parameter not found or instance is invalid
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_blend_texture_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_blend_texture_parameter_value(instance: 'unreal.MaterialInstanceConstant',
                                                        parameter_name: str, layer_index: int,
                                                        value: 'unreal.Texture') -> bool:
        """
        Set the value of a texture parameter in a specific blend layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the blend layer containing the parameter
            value (unreal.Texture): New texture value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_blend_texture_parameter_value(instance, parameter_name, layer_index, value)

    @staticmethod
    def get_layered_material_blend_channel_mask_parameter_value(instance: 'unreal.MaterialInstance',
                                                            parameter_name: str,
                                                            layer_index: int) -> 'unreal.LinearColor':
        """
        Get the value of a channel mask parameter from a specific blend layer.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            layer_index (int): Index of the blend layer containing the parameter

        Returns:
            unreal.LinearColor: The parameter value. Returns (0,0,0,0) if parameter not found or instance is invalid
        """
        return unreal.LayeredMaterialLibrary.get_layered_material_blend_channel_mask_parameter_value(instance, parameter_name, layer_index)

    @staticmethod
    def set_layered_material_blend_channel_mask_parameter_value(instance: 'unreal.MaterialInstanceConstant',
                                                            parameter_name: str,
                                                            layer_index: int,
                                                            value: 'unreal.LinearColor') -> bool:
        """
        Set the value of a channel mask parameter in a specific blend layer.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            layer_index (int): Index of the blend layer containing the parameter
            value (unreal.LinearColor): New value for the parameter

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_layered_material_blend_channel_mask_parameter_value(instance, parameter_name, layer_index, value)

    # Unlayered Parameters

    @staticmethod
    def get_material_channel_mask_parameter_value(
        instance: 'unreal.MaterialInstance',
        parameter_name: str,
        association: 'unreal.MaterialParameterAssociation' = unreal.MaterialParameterAssociation.GLOBAL_PARAMETER
    ) -> 'unreal.LinearColor':
        """
        Get the value of a channel mask parameter from a material.

        Args:
            instance (unreal.MaterialInstance): The material instance to query
            parameter_name (str): Name of the parameter to get
            association (unreal.MaterialParameterAssociation, optional): Parameter association type.
                Defaults to GlobalParameter.

        Returns:
            unreal.LinearColor: The parameter value. Returns (0,0,0,0) if parameter not found or instance is invalid
        """
        return unreal.LayeredMaterialLibrary.get_material_channel_mask_parameter_value(
            instance,
            parameter_name,
            association
        )

    @staticmethod
    def set_material_channel_mask_parameter_value(
        instance: 'unreal.MaterialInstanceConstant',
        parameter_name: str,
        value: 'unreal.LinearColor',
        association: 'unreal.MaterialParameterAssociation' = unreal.MaterialParameterAssociation.GLOBAL_PARAMETER
    ) -> bool:
        """
        Set the value of a channel mask parameter in a material.

        Args:
            instance (unreal.MaterialInstanceConstant): The material instance to modify
            parameter_name (str): Name of the parameter to set
            value (unreal.LinearColor): New value for the parameter
            association (unreal.MaterialParameterAssociation, optional): Parameter association type.
                Defaults to GlobalParameter.

        Returns:
            bool: True if the parameter was successfully set, False otherwise
        """
        return unreal.LayeredMaterialLibrary.set_material_channel_mask_parameter_value(
            instance,
            parameter_name,
            value,
            association
        )

    # Convenience Methods

    @staticmethod
    def get_any_material_parameter_value(
        instance: 'unreal.MaterialInstance',
        parameter_name: str,
        layer_index: int = 0,
        parameter_type: str = 'scalar',
        parameter_domain: str = 'layer'
    ) -> Union[float, 'unreal.LinearColor', bool, 'unreal.Texture']:
        """
        Get any material parameter value based on type and domain.

        Args:
            instance: The material instance to query
            parameter_name: Name of the parameter to get
            layer_index: Index of the layer containing the parameter (ignored for global parameters)
            parameter_type: Type of parameter ('scalar', 'vector', 'static_switch', 'texture', 'channel_mask')
            parameter_domain: Where to get the parameter from ('layer', 'blend', 'global')

        Returns:
            The parameter value of appropriate type
        """
        # Function mappings for each parameter type and domain
        get_functions = {
            'layer': {
                'scalar': LayeredMaterialLibrary.get_layered_material_scalar_parameter_value,
                'vector': LayeredMaterialLibrary.get_layered_material_vector_parameter_value,
                'static_switch': LayeredMaterialLibrary.get_layered_material_static_switch_parameter_value,
                'texture': LayeredMaterialLibrary.get_layered_material_texture_parameter_value,
                'channel_mask': LayeredMaterialLibrary.get_layered_material_channel_mask_parameter_value
            },
            'blend': {
                'scalar': LayeredMaterialLibrary.get_layered_material_blend_scalar_parameter_value,
                'vector': LayeredMaterialLibrary.get_layered_material_blend_vector_parameter_value,
                'static_switch': LayeredMaterialLibrary.get_layered_material_blend_static_switch_parameter_value,
                'texture': LayeredMaterialLibrary.get_layered_material_blend_texture_parameter_value,
                'channel_mask': LayeredMaterialLibrary.get_layered_material_blend_channel_mask_parameter_value
            },
            'global': {
                'scalar': unreal.MaterialEditingLibrary.get_material_instance_scalar_parameter_value,
                'vector': unreal.MaterialEditingLibrary.get_material_instance_vector_parameter_value,
                'static_switch': unreal.MaterialEditingLibrary.get_material_instance_static_switch_parameter_value,
                'texture': unreal.MaterialEditingLibrary.get_material_instance_texture_parameter_value,
                'channel_mask': LayeredMaterialLibrary.get_material_channel_mask_parameter_value
            }
        }

        func = get_functions.get(parameter_domain, {}).get(parameter_type)
        if not func:
            raise ValueError(f"Invalid parameter_type '{parameter_type}' or parameter_domain '{parameter_domain}'")

        if parameter_domain == 'global':
            return func(instance, parameter_name)
        else:
            return func(instance, parameter_name, layer_index)

    @staticmethod
    def set_any_material_parameter_value(
        instance: 'unreal.MaterialInstanceConstant',
        parameter_name: str,
        value: Union[float, 'unreal.LinearColor', bool, 'unreal.Texture'],
        layer_index: int = 0,
        parameter_type: str = 'scalar',
        parameter_domain: str = 'layer',
        only_if_different: bool = False
    ) -> bool:
        """
        Set any material parameter value based on type and domain.

        Args:
            instance: The material instance to modify
            parameter_name: Name of the parameter to set
            value: New value for the parameter
            layer_index: Index of the layer containing the parameter (ignored for global parameters)
            parameter_type: Type of parameter ('scalar', 'vector', 'static_switch', 'texture', 'channel_mask')
            parameter_domain: Where to set the parameter ('layer', 'blend', 'global')
            only_if_different: Only set the parameter if the new value is different from the current value

        Returns:
            bool: True if the parameter was successfully set
        """
        set_functions = {
            'layer': {
                'scalar': LayeredMaterialLibrary.set_layered_material_scalar_parameter_value,
                'vector': LayeredMaterialLibrary.set_layered_material_vector_parameter_value,
                'static_switch': LayeredMaterialLibrary.set_layered_material_static_switch_parameter_value,
                'texture': LayeredMaterialLibrary.set_layered_material_texture_parameter_value,
                'channel_mask': LayeredMaterialLibrary.set_layered_material_channel_mask_parameter_value
            },
            'blend': {
                'scalar': LayeredMaterialLibrary.set_layered_material_blend_scalar_parameter_value,
                'vector': LayeredMaterialLibrary.set_layered_material_blend_vector_parameter_value,
                'static_switch': LayeredMaterialLibrary.set_layered_material_blend_static_switch_parameter_value,
                'texture': LayeredMaterialLibrary.set_layered_material_blend_texture_parameter_value,
                'channel_mask': LayeredMaterialLibrary.set_layered_material_blend_channel_mask_parameter_value
            },
            'global': {
                'scalar': unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value,
                'vector': unreal.MaterialEditingLibrary.set_material_instance_vector_parameter_value,
                'static_switch': unreal.MaterialEditingLibrary.set_material_instance_static_switch_parameter_value,
                'texture': unreal.MaterialEditingLibrary.set_material_instance_texture_parameter_value,
                'channel_mask': LayeredMaterialLibrary.set_material_channel_mask_parameter_value
            }
        }

        func = set_functions.get(parameter_domain, {}).get(parameter_type)
        if not func:
            raise ValueError(f"Invalid parameter_type '{parameter_type}' or parameter_domain '{parameter_domain}'")

        if only_if_different:
            # Get current value
            current_value = LayeredMaterialLibrary.get_any_material_parameter_value(
                instance,
                parameter_name,
                layer_index,
                parameter_type,
                parameter_domain)

            # Compare values based on type
            if parameter_type == 'scalar':
                if abs(current_value - value) < 0.0001:  # Use small epsilon for float comparison
                    return True
            elif parameter_type in ('vector', 'channel_mask'):
                # For LinearColor, compare each component
                if (abs(current_value.r - value.r) < 0.0001 and
                    abs(current_value.g - value.g) < 0.0001 and
                    abs(current_value.b - value.b) < 0.0001 and
                    abs(current_value.a - value.a) < 0.0001):
                    return True
            elif parameter_type == 'static_switch':
                if current_value == value:
                    return True
            elif parameter_type == 'texture':
                if current_value == value:  # Direct comparison for texture references
                    return True

        # Set the new value if we get here
        if parameter_domain == 'global':
            return func(instance, parameter_name, value)
        else:
            return func(instance, parameter_name, layer_index, value)

    @staticmethod
    def get_any_parameter_source(
        instance: 'unreal.MaterialInstance',
        parameter_name: str,
        parameter_type: str = 'scalar'
    ) -> Optional[str]:
        """
        Get the source asset path where a parameter was defined.

        Args:
            instance: Material instance to query
            parameter_name: Name of parameter to look up
            parameter_type: Type of parameter ('scalar', 'vector', 'static_switch', 'texture')

        Returns:
            Optional[str]: Path to the asset where parameter was defined, or None
        """
        source_funcs = {
            'scalar': unreal.MaterialEditingLibrary.get_scalar_parameter_source,
            'vector': unreal.MaterialEditingLibrary.get_vector_parameter_source,
            'static_switch': unreal.MaterialEditingLibrary.get_static_switch_parameter_source,
            'texture': unreal.MaterialEditingLibrary.get_texture_parameter_source
        }

        if parameter_type not in source_funcs:
            return None

        return source_funcs[parameter_type](instance, parameter_name)

    @staticmethod
    def get_full_material_as_dict(instance: 'unreal.MaterialInstance') -> dict:
        """
        Get a comprehensive dictionary of material information including global parameters,
        layer assets, blend assets, and their respective parameters.

        Args:
            instance: The material instance to query

        Returns:
            dict: A dictionary containing all material information structured as:
                {
                    'global': {
                        'parameters': {...}
                    },
                    'layers': {
                        'layerName': {
                            'layerIndex': int,
                            'layerAsset': {
                                'path': str,
                                'parameters': {...}
                            },
                            'blendAsset': {
                                'path': str,
                                'parameters': {...}
                            }
                        }
                    }
                }
        """
        result = {
            'global': {'parameters': {}},
            'layers': {}
        }

        def get_parameters_for_domain(inst, layer_idx, domain):
            params = {}
            # Get parameter names
            scalar_params = unreal.MaterialEditingLibrary.get_scalar_parameter_names(inst)
            vector_params = unreal.MaterialEditingLibrary.get_vector_parameter_names(inst)
            switch_params = unreal.MaterialEditingLibrary.get_static_switch_parameter_names(inst)
            texture_params = unreal.MaterialEditingLibrary.get_texture_parameter_names(inst)

            def add_param(name, param_type):
                try:
                    value = LayeredMaterialLibrary.get_any_material_parameter_value(
                        inst, name, layer_idx, param_type, domain
                    )
                    param_key = f"{name}_{layer_idx}"
                    params[param_key] = {
                        'value': value,
                        'type': param_type,
                        'domain': domain,
                        'layerIndex': layer_idx,
                        'name': name
                    }
                except:
                    pass

            for name in scalar_params:
                add_param(name, 'scalar')
            for name in vector_params:
                add_param(name, 'vector')
            for name in switch_params:
                add_param(name, 'static_switch')
            for name in texture_params:
                add_param(name, 'texture')

            return params

        # Get global parameters
        result['global']['parameters'] = get_parameters_for_domain(instance, 0, 'global')

        # Get layer information
        layer_count = LayeredMaterialLibrary.get_layer_count(instance)
        for layer_idx in range(layer_count):
            # Get layer and blend assets
            layer_asset = None  # You'll need to implement a way to get the layer asset
            blend_asset = None  # You'll need to implement a way to get the blend asset

            layer_name = f"Layer_{layer_idx}"  # You might want to get actual layer names if possible

            result['layers'][layer_name] = {
                'layerIndex': layer_idx,
                'layerAsset': {
                    'path': layer_asset.get_path_name() if layer_asset else None,
                    'parameters': get_parameters_for_domain(instance, layer_idx, 'layer')
                }
            }

            # Don't add blend asset for base layer
            if layer_idx > 0:
                result['layers'][layer_name]['blendAsset'] = {
                    'path': blend_asset.get_path_name() if blend_asset else None,
                    'parameters': get_parameters_for_domain(instance, layer_idx, 'blend')
                }

        return result

    @staticmethod
    def create_full_material_from_dict(
        instance: 'unreal.MaterialInstanceConstant',
        material_data: dict
    ) -> bool:
        """
        Create or modify a layered material using a comprehensive dictionary of parameters.

        Args:
            instance: Material instance to modify
            material_data: Dictionary containing material definition as returned by get_parameter_info

        Returns:
            bool: True if successful
        """
        try:
            # Set global parameters
            if 'global' in material_data and 'parameters' in material_data['global']:
                for param_info in material_data['global']['parameters'].values():
                    LayeredMaterialLibrary.set_any_material_parameter_value(
                        instance=instance,
                        parameter_name=param_info['name'],
                        value=param_info['value'],
                        parameter_type=param_info['type'],
                        parameter_domain='global'
                    )

            # Process layers
            if 'layers' in material_data:
                for layer_name, layer_data in material_data['layers'].items():
                    layer_idx = layer_data['layerIndex']

                    # Assign layer asset
                    if 'layerAsset' in layer_data and layer_data['layerAsset']['path']:
                        layer_asset = unreal.load_object(None, layer_data['layerAsset']['path'])
                        if layer_asset:
                            LayeredMaterialLibrary.assign_layer_material(
                                instance, layer_idx, layer_asset
                            )

                            # Set layer parameters
                            for param_info in layer_data['layerAsset']['parameters'].values():
                                LayeredMaterialLibrary.set_any_material_parameter_value(
                                    instance=instance,
                                    parameter_name=param_info['name'],
                                    value=param_info['value'],
                                    layer_index=layer_idx,
                                    parameter_type=param_info['type'],
                                    parameter_domain='layer'
                                )

                    # Assign blend asset (skip for base layer)
                    if layer_idx > 0 and 'blendAsset' in layer_data and layer_data['blendAsset']['path']:
                        blend_asset = unreal.load_object(None, layer_data['blendAsset']['path'])
                        if blend_asset:
                            LayeredMaterialLibrary.assign_blend_layer(
                                instance, layer_idx, blend_asset
                            )

                            # Set blend parameters
                            for param_info in layer_data['blendAsset']['parameters'].values():
                                LayeredMaterialLibrary.set_any_material_parameter_value(
                                    instance=instance,
                                    parameter_name=param_info['name'],
                                    value=param_info['value'],
                                    layer_index=layer_idx,
                                    parameter_type=param_info['type'],
                                    parameter_domain='blend'
                                )

            return True
        except Exception as e:
            print(f"Error creating material from dictionary: {e}")
            return False



"""
# Example usage
if __name__ == "__main__":
    instance = unreal.load_object(None, '/Game/AP_MaterialLibrary/CommonMaterial/CommonLayer/testPython')
    new_layer_function = unreal.load_object(None, '/Game/AP_MaterialLibrary/LayerMaterial/ML_Master/ML_PLANAR_LAYER')
    new_blend_layer_function = unreal.load_object(None, '/Game/AP_MaterialLibrary/LayerMaterial/ML_Blend/MLB_PlanarAngleHeightVertexRadialMaskAutoAxe')
    parameter_name = 'Metallic'
    layer_index = 0
    value = .5

    #LayeredMaterialLibrary.refresh_editor_material_instance(instance)
    print(instance)
    print(LayeredMaterialLibrary.get_layer_count(instance))
    LayeredMaterialLibrary.add_material_layer(instance)
    print(LayeredMaterialLibrary.is_layered_material(instance))
    LayeredMaterialLibrary.assign_layer_material(instance, layer_index, new_layer_function)
    layer_index = 1
    LayeredMaterialLibrary.assign_layer_material(instance, layer_index, new_layer_function)
    LayeredMaterialLibrary.assign_blend_layer(instance, layer_index, new_blend_layer_function)
    print(LayeredMaterialLibrary.get_layered_material_scalar_parameter_value(instance, parameter_name, layer_index))
    LayeredMaterialLibrary.set_layered_material_scalar_parameter_value(instance, parameter_name, layer_index, value)
    parameter_name = 'Normal Map ?'
    print(LayeredMaterialLibrary.get_layered_material_static_switch_parameter_value(instance, parameter_name, layer_index))
    LayeredMaterialLibrary.set_layered_material_static_switch_parameter_value(instance, parameter_name, layer_index, True)
    parameter_name = 'Normal_Map'
    print(LayeredMaterialLibrary.get_layered_material_texture_parameter_value(instance, parameter_name, layer_index))
    #LayeredMaterialLibrary.set_layered_material_texture_parameter_value(instance, parameter_name, layer_index, unreal.load_object(None, '/Game/Path/To/Your/Texture'))
"""
