from pysc2.lib import actions, features, units
import numpy as np
import units_new
import math


def bin_array(num, m):
    """Convert a positive integer num into an m-bit bit vector"""
    return np.array(list(np.binary_repr(num).zfill(m))).astype(np.int8)


def get_embedded_obs(feature_units):
    unit_type = []
    #unit_attributes = []
    alliance = []
    current_health = []
    current_shields = []
    current_energy = []
    cargo_space_used = []
    cargo_space_maximum = []
    build_progress = []
    current_health_ratio = []
    current_shield_ratio = []
    current_energy_ratio = []
    display_type = []
    x_position = []
    y_position = []
    is_cloaked = []
    is_powered = []
    is_hallucination = []
    is_active = []
    is_on_screen = []
    is_in_cargo = []
    current_minerals = []
    current_vespene = []
    #mined_minerals = []
    #mined_vespene = []
    assigned_harvesters = []
    ideal_harvesters = []
    weapon_cooldown = []
    order_queue_length = []
    order_1 = []
    order_2 = []
    order_3 = []
    order_4 = []
    buffs = []
    addon_type = []
    order_progress_1 = []
    order_progress_2 = []
    weapon_upgrades = []
    armor_upgrades = []
    shield_upgrades = []
    is_selected = []
    #was_targeted = []
    #print("len(feature_units): " + str(len(feature_units)))
    for unit in feature_units:
      unit_info = str(units.get_unit_type(unit.unit_type))
      unit_info = unit_info.split(".")
      unit_race = unit_info[0]
      unit_name = unit_info[1]
      unit_info = int(units_new.get_unit_type(unit_race, unit_name))
      unit_info_onehot = np.identity(256)[unit_info:unit_info+1]
      unit_type.append(unit_info_onehot[0])

      unit_alliance = unit.alliance
      unit_alliance_onehot = np.identity(5)[unit_alliance:unit_alliance+1]
      alliance.append(unit.alliance)

      #print("min(unit.health, 1500): " + str(min(unit.health, 1500)))
      unit_health = int(math.sqrt(min(unit.health, 1500)))
      #print("unit_health: " + str(unit_health))
      unit_health_onehot = np.identity(39)[unit_health:unit_health+1]
      #print("unit_health_onehot: " + str(unit_health_onehot))
      current_health.append(unit_health_onehot[0])

      unit_shield = int(math.sqrt(min(unit.shield, 1000)))
      unit_shield_onehot = np.identity(31)[unit_shield:unit_shield+1]
      current_shields.append(unit_shield_onehot[0])

      unit_energy = int(math.sqrt(min(unit.energy, 200)))
      unit_energy_onehot = np.identity(31)[unit_energy:unit_energy+1]
      current_energy.append(unit_energy_onehot[0])

      cargo_space_used.append(unit.cargo_space_taken)
      cargo_space_maximum.append(unit.cargo_space_max)

      build_progress.append(unit.build_progress)

      current_health_ratio.append(unit.health_ratio)
      current_shield_ratio.append(unit.shield_ratio)
      current_energy_ratio.append(unit.energy_ratio)

      display_type.append(unit.display_type)

      x_position.append(bin_array(unit.x, 10))
      y_position.append(bin_array(unit.y, 10))

      is_cloaked.append(unit.cloak)
      is_powered.append(unit.is_powered)
      is_hallucination.append(unit.hallucination)
      is_active.append(unit.active)
      is_on_screen.append(unit.is_in_cargo)
      is_in_cargo.append(unit.is_powered)

      current_minerals.append(unit.mineral_contents)
      current_vespene.append(unit.vespene_contents)

      assigned_harvesters_onehot = np.identity(24)[unit.assigned_harvesters:unit.assigned_harvesters+1]
      ideal_harvesters_onehot = np.identity(17)[unit.ideal_harvesters:unit.ideal_harvesters+1]
      assigned_harvesters.append(assigned_harvesters_onehot[0])
      ideal_harvesters.append(ideal_harvesters_onehot[0])

      weapon_cooldown_onehot =  np.identity(32)[unit.weapon_cooldown:unit.weapon_cooldown+1]
      weapon_cooldown.append(weapon_cooldown_onehot[0])

      order_queue_length.append(unit.order_length)
      order_1.append(unit.order_id_0)
      order_2.append(unit.order_id_1)
      order_3.append(unit.order_id_2)
      order_4.append(unit.order_id_3)

      buffs.append([unit.buff_id_0, unit.buff_id_1])

      addon_type.append(unit.addon_unit_type)

      order_progress_1.append(unit.order_progress_0)
      order_progress_2.append(unit.order_progress_1)

      weapon_upgrades_onehot = np.identity(4)[unit.attack_upgrade_level:unit.attack_upgrade_level+1]
      armor_upgrades_onehot = np.identity(4)[unit.armor_upgrade_level:unit.armor_upgrade_level+1]
      shield_upgrades_onehot = np.identity(4)[unit.shield_upgrade_level:unit.shield_upgrade_level+1]

      weapon_upgrades.append(weapon_upgrades_onehot[0])
      armor_upgrades.append(armor_upgrades_onehot[0])
      shield_upgrades.append(shield_upgrades_onehot[0])

      is_selected_onehot = np.identity(2)[unit.is_selected:unit.is_selected+1]
      is_selected.append(is_selected_onehot[0])
    
    '''
    unit_type[0].shape: (256,)
    current_health[0].shape: (39,)
    current_shields[0].shape: (31,)
    current_energy[0].shape: (31,)
    x_position[0].shape: (10,)
    y_position[0].shape: (10,)
    assigned_harvesters[0].shape: (24,)
    ideal_harvesters[0].shape: (17,)
    weapon_cooldown[0].shape: (32,)
    weapon_upgrades[0].shape: (4,)
    armor_upgrades[0].shape: (4,)
    shield_upgrades[0].shape: (4,)
    is_selected[0].shape: (2,)
    
    print("unit_type[0].shape: " + str(unit_type[0].shape))
    print("current_health[0].shape: " + str(current_health[0].shape))
    print("current_shields[0].shape: " + str(current_shields[0].shape))
    print("current_energy[0].shape: " + str(current_energy[0].shape))
    print("x_position[0].shape: " + str(x_position[0].shape))
    print("y_position[0].shape: " + str(y_position[0].shape))
    print("assigned_harvesters[0].shape: " + str(assigned_harvesters[0].shape))
    print("ideal_harvesters[0].shape: " + str(ideal_harvesters[0].shape))
    print("weapon_cooldown[0].shape: " + str(weapon_cooldown[0].shape))
    print("weapon_upgrades[0].shape: " + str(weapon_upgrades[0].shape))
    print("armor_upgrades[0].shape: " + str(armor_upgrades[0].shape))
    print("shield_upgrades[0].shape: " + str(shield_upgrades[0].shape))
    print("is_selected[0].shape: " + str(is_selected[0].shape))
    print("")
    '''
    input_list = []
    #print("len(current_health): " + str(len(current_health)))

    length = len(feature_units)
    if length > 100:
      length = 100

    for i in range(0, length):
      padded_current_health = np.zeros(256)
      padded_current_shields = np.zeros(256)
      padded_current_energy = np.zeros(256)
      padded_current_health[:current_health[i].shape[0]] = current_health[i]
      padded_current_shields[:current_shields[i].shape[0]] = current_shields[i]
      padded_current_energy[:current_energy[i].shape[0]] = current_energy[i]
      input_list.append(padded_current_health)
      input_list.append(padded_current_shields)
      input_list.append(padded_current_energy)

      padded_x_position = np.zeros(256)
      padded_y_position = np.zeros(256)
      padded_x_position[:x_position[i].shape[0]] = x_position[i]
      padded_y_position[:y_position[i].shape[0]] = y_position[i]
      input_list.append(padded_x_position)
      input_list.append(padded_y_position)

      padded_assigned_harvesters = np.zeros(256)
      padded_ideal_harvesters = np.zeros(256)
      padded_assigned_harvesters[:assigned_harvesters[i].shape[0]] = assigned_harvesters[i]
      padded_ideal_harvesters[:ideal_harvesters[i].shape[0]] = ideal_harvesters[i]
      input_list.append(padded_assigned_harvesters)
      input_list.append(padded_ideal_harvesters)

      padded_weapon_cooldown = np.zeros(256)
      padded_weapon_cooldown[:weapon_cooldown[i].shape[0]] = weapon_cooldown[i]
      input_list.append(padded_weapon_cooldown)

      padded_weapon_upgrades = np.zeros(256)
      padded_armor_upgrades = np.zeros(256)
      padded_shield_upgrades = np.zeros(256)
      padded_weapon_upgrades[:weapon_upgrades[i].shape[0]] = weapon_upgrades[i]
      padded_armor_upgrades[:armor_upgrades[i].shape[0]] = armor_upgrades[i]
      padded_shield_upgrades[:shield_upgrades[i].shape[0]] = shield_upgrades[i]
      input_list.append(padded_weapon_upgrades)
      input_list.append(padded_armor_upgrades)
      input_list.append(padded_shield_upgrades)
      
      padded_is_selected = np.zeros(256)
      padded_is_selected[:is_selected[i].shape[0]] = is_selected[i]
      #print("padded_is_selected.shape: " + str(padded_is_selected.shape))
      #print("padded_is_selected: " + str(padded_is_selected))
      input_list.append(padded_is_selected)

      #print("padded_current_health.shape: " + str(padded_current_health.shape))
      #print("padded_current_shields.shape: " + str(padded_current_shields.shape))
      #print("padded_current_energy.shape: " + str(padded_current_energy.shape))
      #print("")

    #print("len(input_list): " + str(len(input_list)))
    input_array = np.array(input_list)
    #print("input_array.shape: " + str(input_array.shape))
    #print("")

    return input_array