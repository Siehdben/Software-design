from hero_builder import HeroBuilder, EnemyBuilder

def main():
    hero_builder = HeroBuilder()
    hero = (hero_builder.set_height(180)
                        .set_body_type("Athletic")
                        .set_hair_color("Blonde")
                        .set_eye_color("Blue")
                        .set_clothing("Armor")
                        .set_inventory(["Sword", "Shield"])
                        .build())

    enemy_builder = EnemyBuilder()
    enemy = (enemy_builder.set_height(190)
                          .set_body_type("Muscular")
                          .set_hair_color("Black")
                          .set_eye_color("Red")
                          .set_clothing("Dark Armor")
                          .set_inventory(["Axe", "Dagger"])
                          .set_evil_plan("World Domination")
                          .build())

    print(hero)
    print(enemy)

if __name__ == "__main__":
    main()
