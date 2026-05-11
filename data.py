import os

IMAGES_DIR = "images"

animals = {
    "lesser_eagle": {
        "name": "Малый подорлик",
        "emoji": "🦅",
        "description": (
            "Лесной орёл с острым взглядом и спокойным, но решительным характером. "
            "Ты - наблюдательный стратег, который умеет видеть картину целиком и никогда не торопится с выводами. "
            "Свобода и независимость для тебя важнее любых удобств."
        ),
        "image": os.path.join(IMAGES_DIR, "lesser_eagle.jpg"),
        "link": "https://moscowzoo.ru/animals/kinds/malyy_podorlik",
    },
    "blue_macaw": {
        "name": "Сине-жёлтый ара",
        "emoji": "🦜",
        "description": (
            "Яркий, общительный и очень умный попугай. "
            "Ты любишь внимание, умеешь расположить к себе любого и всегда выделяешься в компании. "
            "Скучать рядом с тобой точно не придётся!"
        ),
        "image": os.path.join(IMAGES_DIR, "blue_macaw.jpg"),
        "link": "https://moscowzoo.ru/animals/kinds/sine_zheltyy_ara",
    },
    "toco_toucan": {
        "name": "Большой тукан",
        "emoji": "🐦",
        "description": (
            "Экзотический и харизматичный. "
            "Ты яркий, оптимистичный и обладаешь отличным чувством юмора. "
            "Жизнь для тебя - это праздник, и ты умеешь заряжать этим настроением всех вокруг."
        ),
        "image": os.path.join(IMAGES_DIR, "toco_toucan.jpg"),
        "link": "https://moscowzoo.ru/animals/kinds/bolshoy_tukan",
    },
    "short_eared_owl": {
        "name": "Болотная сова",
        "emoji": "🦉",
        "description": (
            "Ночная охотница с отличной интуицией. "
            "Ты независимый и скрытный - и прекрасно ориентируешься в любой ситуации, даже в полной темноте. "
            "Твоя сила - в умении слушать и замечать то, что другие пропускают мимо."
        ),
        "image": os.path.join(IMAGES_DIR, "short_eared_owl.jpg"),
        "link": "https://moscowzoo.ru/animals/kinds/bolotnaya_sova",
    },
    "stanley_crane": {
        "name": "Журавль Стэнли",
        "emoji": "🦢",
        "description": (
            "Грациозный и благородный. "
            "Ты элегантен во всём - в словах, в поступках, в стиле. "
            "Сильное чувство собственного достоинства и любовь к красоте делают тебя настоящим аристократом среди птиц."
        ),
        "image": os.path.join(IMAGES_DIR, "stanley_crane.jpg"),
        "link": "https://moscowzoo.ru/animals/kinds/zhuravl_stenli",
    },
    "red_flamingo": {
        "name": "Красный фламинго",
        "emoji": "🦩",
        "description": (
            "Яркий, социальный и очень стильный. "
            "Ты любишь быть в центре внимания и всегда выглядишь эффектно. "
            "Фламинго живут большими стаями - как и ты, они не представляют жизни без тёплой компании."
        ),
        "image": os.path.join(IMAGES_DIR, "red_flamingo.jpg"),
        "link": "https://moscowzoo.ru/animals/kinds/krasnyy_flamingo",
    },
    "jungle_cat": {
        "name": "Камышовый кот",
        "emoji": "🐈",
        "description": (
            "Сильный, независимый и смелый охотник. "
            "Ты любишь свободу, приключения и хорошо адаптируешься к любой среде. "
            "Камышовый кот - один из немногих диких котов, который не боится воды. Узнаёшь себя?"
        ),
        "image": os.path.join(IMAGES_DIR, "jungle_cat.jpg"),
        "link": "https://moscowzoo.ru/animals/kinds/kamyshovyy_kot",
    },
    "forest_polecat": {
        "name": "Лесной хорёк",
        "emoji": "🐾",
        "description": (
            "Ловкий, любопытный и очень энергичный. "
            "Ты быстрый, предприимчивый и всегда находишь выход из любой ситуации. "
            "Скуки для тебя не существует - каждый день нужно исследовать что-то новое!"
        ),
        "image": os.path.join(IMAGES_DIR, "forest_polecat.jpg"),
        "link": "https://moscowzoo.ru/animals/kinds/lesnoy_horek",
    },
}

questions = [
    {
        "id": 1,
        "text": "🌅 Какой образ жизни тебе ближе?",
        "answers": [
            {"text": "Активный - люблю движение и приключения", "animal_points": {"jungle_cat": 3, "forest_polecat": 2}},
            {"text": "Спокойный и наблюдательный", "animal_points": {"lesser_eagle": 3, "short_eared_owl": 2}},
            {"text": "Общительный - люблю быть среди людей", "animal_points": {"blue_macaw": 3, "red_flamingo": 2}},
            {"text": "Грациозный и размеренный", "animal_points": {"stanley_crane": 3, "toco_toucan": 1}},
        ],
    },
    {
        "id": 2,
        "text": "💪 Какое качество в тебе самое сильное?",
        "answers": [
            {"text": "Независимость и сила", "animal_points": {"jungle_cat": 3, "lesser_eagle": 2}},
            {"text": "Яркость и харизма", "animal_points": {"blue_macaw": 3, "red_flamingo": 2, "toco_toucan": 1}},
            {"text": "Интуиция и наблюдательность", "animal_points": {"short_eared_owl": 3, "lesser_eagle": 1}},
            {"text": "Элегантность и достоинство", "animal_points": {"stanley_crane": 3, "red_flamingo": 1}},
        ],
    },
    {
        "id": 3,
        "text": "🏡 Где ты чувствуешь себя лучше всего?",
        "answers": [
            {"text": "В лесу или на природе", "animal_points": {"lesser_eagle": 3, "jungle_cat": 2, "forest_polecat": 2}},
            {"text": "Среди людей и ярких событий", "animal_points": {"blue_macaw": 3, "red_flamingo": 2, "toco_toucan": 2}},
            {"text": "На открытых просторах", "animal_points": {"stanley_crane": 3, "short_eared_owl": 2}},
            {"text": "У воды - у реки, озера, моря", "animal_points": {"short_eared_owl": 2, "jungle_cat": 2}},
        ],
    },
    {
        "id": 4,
        "text": "😄 Какой у тебя характер?",
        "answers": [
            {"text": "Любопытный и озорной", "animal_points": {"forest_polecat": 3, "blue_macaw": 2}},
            {"text": "Спокойный стратег", "animal_points": {"lesser_eagle": 3, "short_eared_owl": 2}},
            {"text": "Яркий и эмоциональный", "animal_points": {"red_flamingo": 3, "toco_toucan": 2}},
            {"text": "Сильный и самодостаточный", "animal_points": {"jungle_cat": 3, "stanley_crane": 1}},
        ],
    },
    {
        "id": 5,
        "text": "❤️ Что ты ценишь в жизни больше всего?",
        "answers": [
            {"text": "Свободу и независимость", "animal_points": {"jungle_cat": 3, "lesser_eagle": 2}},
            {"text": "Общение и яркие эмоции", "animal_points": {"blue_macaw": 3, "red_flamingo": 2, "toco_toucan": 2}},
            {"text": "Тишину и внутреннюю гармонию", "animal_points": {"short_eared_owl": 3, "stanley_crane": 2}},
            {"text": "Движение и новые открытия", "animal_points": {"forest_polecat": 3, "jungle_cat": 1}},
        ],
    },
    {
        "id": 6,
        "text": "🧩 Как ты обычно решаешь проблемы?",
        "answers": [
            {"text": "Действую напрямую, без раздумий", "animal_points": {"jungle_cat": 3, "forest_polecat": 2}},
            {"text": "Долго наблюдаю, потом действую", "animal_points": {"lesser_eagle": 3, "short_eared_owl": 2}},
            {"text": "Ищу нестандартные решения", "animal_points": {"toco_toucan": 3, "blue_macaw": 2}},
            {"text": "Полагаюсь на интуицию и опыт", "animal_points": {"short_eared_owl": 2, "stanley_crane": 2}},
        ],
    },
    {
        "id": 7,
        "text": "🌙 Какое время суток тебе нравится больше?",
        "answers": [
            {"text": "Утро - свежесть и начало нового дня", "animal_points": {"red_flamingo": 2, "stanley_crane": 2, "lesser_eagle": 1}},
            {"text": "День - в самом разгаре жизни", "animal_points": {"toco_toucan": 2, "blue_macaw": 2}},
            {"text": "Вечер и ночь - моё время", "animal_points": {"short_eared_owl": 3, "jungle_cat": 2}},
            {"text": "Не важно - я активен всегда!", "animal_points": {"forest_polecat": 3, "blue_macaw": 2}},
        ],
    },
    {
        "id": 8,
        "text": "🧠 Ты больше...",
        "answers": [
            {"text": "Интроверт - заряжаюсь в одиночестве", "animal_points": {"short_eared_owl": 3, "lesser_eagle": 2, "jungle_cat": 1}},
            {"text": "Экстраверт - заряжаюсь от общения", "animal_points": {"blue_macaw": 3, "red_flamingo": 3, "toco_toucan": 2}},
            {"text": "Амбиверт - зависит от настроения", "animal_points": {"stanley_crane": 2, "forest_polecat": 2}},
        ],
    },
    {
        "id": 9,
        "text": "🎯 Какое у тебя любимое занятие?",
        "answers": [
            {"text": "Исследовать новые места и идеи", "animal_points": {"forest_polecat": 3, "jungle_cat": 2}},
            {"text": "Общаться с друзьями и близкими", "animal_points": {"blue_macaw": 3, "red_flamingo": 2}},
            {"text": "Наблюдать и размышлять", "animal_points": {"lesser_eagle": 3, "short_eared_owl": 2}},
            {"text": "Создавать красивое вокруг себя", "animal_points": {"stanley_crane": 3, "toco_toucan": 1}},
        ],
    },
    {
        "id": 10,
        "text": "🔄 Как ты относишься к рутине?",
        "answers": [
            {"text": "Не люблю - быстро устаю от однообразия", "animal_points": {"forest_polecat": 3, "blue_macaw": 2}},
            {"text": "Нормально, если есть смысл и цель", "animal_points": {"stanley_crane": 2, "lesser_eagle": 2}},
            {"text": "Предпочитаю свободу и разнообразие", "animal_points": {"jungle_cat": 3, "toco_toucan": 2}},
            {"text": "Мне нужны ритм и предсказуемость", "animal_points": {"short_eared_owl": 2, "red_flamingo": 1}},
        ],
    },
]