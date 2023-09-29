import { globby } from 'globby';
import fm from 'front-matter';
import { readFile, writeFile } from 'fs/promises';
import path from 'path';
import {optimize} from 'svgo'

let icon_sets = ["./public/icons"]
for (let sets of icon_sets){

    let files = await globby(`${sets}/*.svg`);
    files = files.filter(item => {return !item.toString().endsWith("/_sprite.svg")})

    const sprite = await Promise.all(
      files.map(async file => {
        const name = path.basename(file, path.extname(file));
        const data = fm(await readFile(file, 'utf8'));

        let opti_svg = optimize(data['body'],{multipass:true, plugins: ['preset-default',{"name":"removeDimensions"}, {"name":"convertStyleToAttrs"}]}) //

        await writeFile(path.join(sets, path.basename(file)), opti_svg.data, 'utf8');

        let svgcode = opti_svg.data
        //svgcode = svgcode.toString().replace(/<title>.*?<\/title>/g, '');
        //svgcode = svgcode.toString().replace(/<style>.*?<\/style>/g, '');
        //svgcode = svgcode.toString().replace(/#fff/g, 'currentcolor');
        //svgcode = svgcode.toString().replace(/#FFFFFF/g, 'currentcolor');
        svgcode = svgcode.replace((/<svg/g), `<svg id="${name}"`)

        return svgcode

      })
    );

    await writeFile(
      path.join(sets, '_sprite.svg'),
      `<?xml version="1.0" encoding="utf-8"?><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">${sprite.join("")}</svg>`,
      'utf8'
    );
    console.log(`SVG Optimization for ${sets} finished`)
}
